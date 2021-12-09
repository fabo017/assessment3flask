### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

A. JavaScript is standardized in ECMAScript, whereas Python is not. JavaScript does not support procedural programming, whereas Python does. Python syntax is cleaner and easier to read and implement. Python also comes with many modules and packages that you can import. Python has  a concept of mutables and immutables, whereas JavaScript does not.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

Answer: Use method get() or setdefault()

- What is a unit test?

Answer: Testing phase that test individual units of code to see if they work properly. Happens before integration testing. 

- What is an integration test?

Answer: Testing phase that takes place after unit testing. The individual modules used in the code are tested to see if they work correctly or not by combining and testing them as groups.
 
- What is the role of web application framework, like Flask?

Answer: Flask provides tools, libraries, and technologies to be used to build web applications with little to no dependencies on externals libraries. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Answer: I would use query params when using API request to retrieve data and to sort/filter data or represent a certain page.

- How do you collect data from a URL placeholder parameter using Flask?

Answer: Use flask.request.args.get('param')

- How do you collect data from the query string using Flask?

Answer: Use flask.request.query_string

- How do you collect data from the body of the request using Flask?

Answer: Use flask.request.data

- What is a cookie and what kinds of things are they commonly used for?

Answer: Cookies are text sent to browser from website to remember certain data for reoccurring visits and are used to make websites better for you.

- What is the session object in Flask?

Answer: Session object is a dictionary object that tracks a session and has key-value pairs of variables from the session as keys and the values are the corresponding data.

- What does Flask's `jsonify()` do?

Answer: It serializes data into JSON and wraps it into a response object.
