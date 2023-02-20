
## INFO_HUB deals with News and MCQs &nbsp;<img src="https://user-images.githubusercontent.com/125151906/220065960-b3a4fb32-bba8-4882-bb54-ecc3f2c19a7b.png" width="35" height="30">



## Tables Contains:
- [Overview](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Appearence](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Project Architechture](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Directory Tree](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Requirements](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [API Referrence](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Tech Stack](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Credits](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)

## Overview
This is a News and Current Affairs Website that shows Worlds Top News and Quention Answers based on the topic that user selects form the dropdown. This is developed using Flask on backend and HTML5,CSS3 and Javascript on the Front End integarted with two Application Program Inteface.

## Appearance : 
<p align="left"><img src="https://user-images.githubusercontent.com/125151906/220062212-dd0509d7-bb78-475b-ba30-00eac29ba80b.png" width="620" height="350"><p align=right>
<img src="https://user-images.githubusercontent.com/125151906/220062420-4566e703-b9d5-4311-97fb-5c056f5ff250.png" width="620" height="350"></p></p>

## Project Architechture :
<p align="left"><img src="https://user-images.githubusercontent.com/125151906/220064416-01668612-e6d7-4ca6-8926-0c69db8f3e66.jpeg" width="630" height="400" ></p>

## Directory Tree
├── app --(.py)<br>
├── templates -> ✓ layout<br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ index <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ allnews <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ allnews_2 <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ CS <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ GK <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ GO <br>
                  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;  ✓ SP <br>
                
├── static  -> ✓ CSS <br>
                 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; ✓ JS <br>
                 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; ✓ fav <br>


## Requirements
✓ Python 3.10.4 <br>
✓ Flask==2.2.2 <br>
✓ requests==2.27.1

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. gf56553ffdd |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

![Logo](data:image/png;base64,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)
