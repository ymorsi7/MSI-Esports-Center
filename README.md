<img src = "https://cdn.dribbble.com/users/3144264/screenshots/16080159/media/76c03dd932c1e3f797c3fb5869826de9.png"  height = "75"> <img src = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Seal_of_the_University_of_California%2C_San_Diego.svg/1200px-Seal_of_the_University_of_California%2C_San_Diego.svg.png"  height = "75">

# MSI Hackathon (UC San Diego)

In this hackathon, our assigned challenge was to create a solution that enhances the efficiency of Triton Esports Center (TEC) operations by tracking and managing user session times at PCs. The goal of this challenge is to improve queue times for patrons and streamline the overall organization of the TEC usage.

Features that we were recommended to include, and decided to work on, were:
- queue management with ID scanning
- user session tracking for each PC
- scalability (PC layout and statuses can be managed)

We also decided to include:
- an AI-chat bot for the student worker that gives them information about the data
- user interface for user selecting seats
- data analytics (time series analysis on the guests)
  - can be exported to PDF
- metrics tracking for guests (keeping track of how long they stay and scoring the credibility of guests
- [timer for the students using computers]([[https://tecguest.netlify.app/]](https://tecguest.netlify.app/))


## About


```python
binClfr = [] # list (0 or 1)
numHate = 0 # a counter for the number of hate comments
for i in range(len(commentsList)):
    inp = cv.transform([commentsList[i]]).toarray()
    if (model.predict(inp) == ['Offensive Speech']):
        binClfr.append(1) # add one if offensive
        numHate += 1
    elif (model.predict(inp) == ['No Hate and Offensive Speech']):
        binClfr.append(0) # add zero if comment is not hate speech
    else:
        binClfr.append(9) # Add 9 if output it neither (shouldn't happen; means that there's an error)
    print(model.predict(inp))
```

## Hate Speech Detection Resul
