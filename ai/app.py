from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

def sentiment_analysis(api_key, text):
    openai.api_key = api_key
    messages = [
        {"role": "system", "content": "You are a helpful assistant and will provide information about analytics of the csv data i feed you."},
        {"role": "user", "content": f"Analyze the following csv (where severe, moderate, and light and levels of strikes that the people have for staying too long in the esports center). NOTE THAT I WANT INFORMATION ABOUT THE INDIVIDUAL STUDENTS AND THE TIMES THEY GOT THERE, NOT ABOUT THE PROMPT: '{text}'"}
    ]
    
    try:
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        return response['choices'][0]['message']['content'].strip()
    except openai.error.OpenAIError as e:
        return f"Error in fetching response: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    text = None
    api_key = None
    if request.method == 'POST':
        api_key = 'sk-PRIVATE'
        text = '''PID,Name,Time In,Total Hours (H), Extra Time (Minutes), Severe, Moderate, Light
        A86513003,Christopher Hoag,2023-11-18 03:53:12,1,3,0,1,2
        A24945316,Ivan Dillehay,2023-11-18 02:00:10,1,19,0,0,2
        A29475511,Charles Linton,2023-11-18 20:21:06,4,13,1,0,1
        A45573227,Roy Mingle,2023-11-18 02:22:59,1,60,1,2,0
        A93493591,Jose Hussey,2023-11-18 14:29:36,3,40,1,1,3
        A69568879,Leo Spegal,2023-11-18 14:51:51,4,6,0,0,1
        A66600850,Steven Pinkerton,2023-11-18 20:09:02,4,24,0,2,2
        A29089427,Joseph Erdmann,2023-11-18 14:15:30,1,54,1,1,2
        A96886280,James Leggitt,2023-11-18 13:26:29,2,56,1,1,1
        '''
    sentiment = sentiment_analysis(api_key, text)
    
    return render_template('index.html', sentiment=sentiment, text=text, api_key=api_key)

if __name__ == '__main__':
    app.run(debug=True)
