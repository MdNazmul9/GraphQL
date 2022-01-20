# GraphQL

#### User Registration
```
mutation{
  register(
    email: "mn@mn.com",
    username: "mn",
    password1: "Mn7854LKJ",
    password2: "Mn7854LKJ"
  ){
    success,
    errors,
    token,
    refreshToken,
  }
}
```

#### Logged User
```
{
  me {
    username
    email
  }
}
```
#### Emailed Token
```
eyJ1c2VybmFtZSI6Im1ubm4iLCJhY3Rpb24iOiJhY3RpdmF0aW9uIn0:1nAE5S:y5_aM8PlM3RcY_J4sQF6zqQ7Tmm-z1sp9no7A2Vdm84
```

#### Verify Account
```
mutation{
  verifyAccount(token: "eyJ1c2VybmFtZSI6Im1ubm4iLCJhY3Rpb24iOiJhY3RpdmF0aW9uIn0:1nAE5S:y5_aM8PlM3RcY_J4sQF6zqQ7Tmm-z1sp9no7A2Vdm84")
	{
    success
    errors
  }
}
```

#### Login user 
```
mutation{
  tokenAuth(username: "mn48", password: "testpass1234"){
    success
    errors
    token
    refreshToken
    user{
      username
    }
  }
}
```

#### Update

```
mutation{
  updateAccount(firstName:"MdNazmulHossain")
  {
    success
    errors
  }
}
```

# [Help](https://django-graphql-auth.readthedocs.io/en/latest/)