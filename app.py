from flask import Flask, render_template, request
from flask import Response

# from flask import send_file
# import os

app = Flask(__name__)


# Define your routes and logic


@app.route("/download", methods=["POST"])
def download():
    data = request.form.get("data")

    if data:
        filename = "extracted_data.txt"

        # Set the appropriate headers for a text file download
        headers = {
            "Content-Disposition": f"attachment; filename={filename}",
            "Content-Type": "text/plain",
        }

        # Create a Response object with the file content and headers
        response = Response(data, headers=headers)

        return response

    return "No data to download."


# @app.route("/download", methods=["POST"])
# def download():
#     data = request.form.getlist("data[]")

#     if data:
#         file_content = "\n".join(data)

#         # Save the data to a temporary file
#         temp_file = "extracted_data.txt"
#         with open(temp_file, "w") as file:
#             file.write(file_content)

#         # Download the temporary file
#         return send_file(temp_file, as_attachment=True)

#     return "No data to download."


@app.route("/search", methods=["POST"])
def search():
    perno = request.form.get("perno")
    file = request.files["file"]

    if file:
        file_content = file.read().decode("utf-8")

        lines = file_content.split("\n")
        index = None
        for i, line in enumerate(lines):
            if perno in line:
                index = i
                break

        if index is not None:
            data = lines[index : index + 27]
        else:
            data = None

        return render_template("result.html", data=data)

    return "No file selected."


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/search", methods=["POST"])
# def search():
#     perno = request.form.get("perno")

#     with open("data.txt", "r") as file:
#         lines = file.readlines()
#         index = None
#         for i, line in enumerate(lines):
#             if perno in line:
#                 index = i
#                 break

#         if index is not None:
#             data = lines[index : index + 27]
#         else:
#             data = None

#     return render_template("result.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
