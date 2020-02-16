

# Deekoo auth

This holds backend code for the website https://deekoo.netlify.com

There authenticated users can see events added by others on the map

## Installation



## Available routes



### Authentication and admin

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


