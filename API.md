

# Deekoo auth

This holds backend code for the website https://deekoo.netlify.com

There authenticated users can see events added by others on the map

## Installation



## Available routes



### Authentication and admin



```
Server                      React web app

                  no token
/map            ◄---------  Ask for protected 
     |                       data from api
     |                              
     ▼                              
No valid 
access token    ---------►    Fine...
                                 |
                                 |
                                 ▼                                    
/authenticate   ◄---------    Login page
     |
     |
     ▼              token
generate token  ---------►   Store obtained token
                              to secure cookies
```

After obtaining a valid token, we access content with the token

```
Server                      React web app

                with token
/map            ◄---------  Ask for protected 
     |                       data from api
     |                              
     ▼                              
Is valid 
access token    ---------►    gets content 😊 

```
                                    


Authenticate takes in a valid webtoken, if old webtoken given, the user is prompted to request new to their email. 

```python
@app.route("/authenticate", methods=["POST"])      
```

Admin can invite new users to the group

```python
@app.route("/users", methods=["POST"])      
@admin_required
```

### Map

Gives authenticated users the events on the map

```python
@app.route("/map", methods=["GET"])      
@login_required
```

Allows adding new events on the map

```python
@app.route("/map", methods=["POST"])      
@login_required
```


