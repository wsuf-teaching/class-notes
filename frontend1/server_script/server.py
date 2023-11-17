from flask import Flask, request

app = Flask(__name__)

# this is the endpoint "/test" that you have to target, and currently it allows both "GET" and "POST" methods
@app.route('/test', methods=['GET','POST'])
def test_endpoint():
    # Grab the posted data
    posted_data = request.form.to_dict()

    # Print the posted data line by line one key at a time
    for key, value in posted_data.items():
        print(f"{key}: {value}")

    # if the data you sent has both "name" and "age", respond something different to your page
    if 'name' in posted_data and 'age' in posted_data:
        return f"Your name is: {posted_data['name']}. Your age is almost {int(posted_data['age'])+1}"


    # You can process the data further if needed
    # .. if you know python :)

    # Send a response otherwise (you can customize this as needed)
    return 'Data received successfully!'

# by default, the server run on port 5000, but you can override it here to any unused port in your system.
if __name__ == '__main__':
    app.run(debug=True,port=5000)