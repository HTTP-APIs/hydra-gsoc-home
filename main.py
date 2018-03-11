from flask import Flask, request, jsonify, make_response, render_template, redirect
import yaml

DEBUG = False
app = Flask(__name__)
app.debug = DEBUG

@app.route('/')
def handler():
    # load a YAML file with text content
    with open("content.yaml", 'r') as stream:
        try:
            yaml_text = yaml.load(stream)
        except yaml.YAMLError as exc:
            raise exc
    # parse the YAML file into a variables
    idea = yaml_text['content']
    total = len(idea)
    return render_template("index.html", idea=idea, total=total)


if __name__ == '__main__':
	app.run()
