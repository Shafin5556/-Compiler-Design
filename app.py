from flask import Flask, render_template, request
import re
app = Flask(__name__)


@app.route('/')
def index():
    problems = [
        {"id": 1, "title": "Test whether a given identifier is valid or not."},
        {"id": 2, "title": "Count and show the max frequency of a word in a string."},
        {"id": 3, "title": "Count lines, identify comments, and remove them from input text."},
        {"id": 4, "title": "Identify and count the articles in a given string."},
        {"id": 5, "title": "Validate a set of identifiers."},
        {"id": 6, "title": "Extract and count the prepositions from a given string."},
        {"id": 7, "title": "Check if a text matches a given regular expression."},
    ]
    return render_template('index.html', problems=problems)




@app.route('/problem1', methods=['GET', 'POST'])
def problem1():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            identifier = request.form.get('input_text', '')
            if identifier.isidentifier():
                output = f"'{identifier}' is a valid identifier."
            else:
                output = f"'{identifier}' is not a valid identifier."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem1.html', output=output)


# Problem 2 Page
@app.route('/problem2', methods=['GET', 'POST'])
def problem2():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            text = request.form.get('input_text', '')
            if text.strip():  # Ensure input is not empty
                words = text.split()
                word_freq = {word: words.count(word) for word in set(words)}
                max_count = max(word_freq.values())
                most_frequent_words = [word for word, count in word_freq.items() if count == max_count]
                
                output = (f"The most frequent word(s): {', '.join(most_frequent_words)} "
                          f"with a count of {max_count}.")
            else:
                output = "No input text provided. Please enter some text."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem2.html', output=output)



@app.route('/problem3', methods=['GET', 'POST'])
def problem3():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            # Get the input text from the user
            text = request.form.get('input_text', '')
            if text.strip():  # Ensure input is not empty
                # Split the input into lines
                lines = text.splitlines()
                total_lines = len(lines)
                
                # Identify and remove comments
                processed_lines = []
                in_multiline_comment = False
                for line in lines:
                    stripped_line = line.strip()
                    
                    # Check for multiline comment start and end
                    if stripped_line.startswith("/*"):
                        in_multiline_comment = True
                        continue
                    if stripped_line.endswith("*/"):
                        in_multiline_comment = False
                        continue
                    
                    # Ignore single-line comments or lines within multiline comments
                    if in_multiline_comment or stripped_line.startswith("//"):
                        continue
                    
                    # Add non-comment lines
                    processed_lines.append(line)
                
                # Prepare output
                non_comment_text = "\n".join(processed_lines)
                output = (f"Total lines: {total_lines}\n"
                          f"Non-comment lines:\n{non_comment_text}")
            else:
                output = "No input text provided. Please enter some text."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem3.html', output=output)

@app.route('/problem4', methods=['GET', 'POST'])
def problem4():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            # Get the input text
            text = request.form.get('input_text', '')
            if text.strip():  # Ensure input is not empty
                # Tokenize the input and count articles
                words = text.lower().split()
                articles = ['a', 'an', 'the']
                article_counts = {article: words.count(article) for article in articles}
                total_articles = sum(article_counts.values())
                
                # Prepare the output
                article_details = ", ".join([f"'{article}': {count}" for article, count in article_counts.items()])
                output = (f"Total articles found: {total_articles}\n"
                          f"Breakdown: {article_details}")
            else:
                output = "No input text provided. Please enter some text."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem4.html', output=output)

@app.route('/problem5', methods=['GET', 'POST'])
def problem5():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            # Get the input text
            text = request.form.get('input_text', '')
            if text.strip():  # Ensure input is not empty
                # Split the input into identifiers
                identifiers = [identifier.strip() for identifier in text.replace(',', ' ').split()]
                
                # Validate each identifier
                results = {}
                for identifier in identifiers:
                    if identifier.isidentifier():
                        results[identifier] = "Valid"
                    else:
                        results[identifier] = "Invalid"
                
                # Format the output
                output = "\n".join([f"'{identifier}': {status}" for identifier, status in results.items()])
            else:
                output = "No input text provided. Please enter some identifiers."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem5.html', output=output)

@app.route('/problem6', methods=['GET', 'POST'])
def problem6():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            # Get the input text
            text = request.form.get('input_text', '')
            if text.strip():  # Ensure input is not empty
                # List of common prepositions
                prepositions_list = [
                    "in", "on", "at", "by", "with", "under", "over", "through", "between", "about",
                    "against", "before", "after", "during", "of", "for", "to", "from", "as", "into",
                ]
                
                # Tokenize the input and count prepositions
                words = text.lower().split()
                prepositions = [word for word in words if word in prepositions_list]
                count_prepositions = len(prepositions)
                
                # Format the output
                output = (f"Total prepositions found: {count_prepositions}\n"
                          f"Prepositions: {', '.join(prepositions)}")
            else:
                output = "No input text provided. Please enter some text."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem6.html', output=output)

@app.route('/problem7', methods=['GET', 'POST'])
def problem7():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'run':
            # Get the regex pattern and the input text from the user
            regex_pattern = request.form.get('regex_pattern', '')
            input_text = request.form.get('input_text', '')

            if regex_pattern.strip() and input_text.strip():  # Ensure inputs are not empty
                try:
                    # Check if the input text matches the regex pattern
                    if re.match(regex_pattern, input_text):
                        output = f"The input text matches the pattern: '{regex_pattern}'."
                    else:
                        output = f"The input text does NOT match the pattern: '{regex_pattern}'."
                except re.error:
                    output = "Invalid regular expression pattern. Please enter a valid regex."
            else:
                output = "Both regex pattern and input text are required."
        elif action == 'pause':
            output = "Execution paused. You can resume by pressing 'Run'."
    return render_template('problem7.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
