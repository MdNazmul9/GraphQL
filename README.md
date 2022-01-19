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
