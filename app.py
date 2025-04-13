from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Predefined username and password
USERNAME = "admin"
PASSWORD = "password"

df = pd.read_csv(r"C:\Users\devap\Student ResultAnalysis\Expanded_data_with_more_features.csv")
df.drop("Unnamed: 0", axis=1, inplace=True)

# Function to save plots
def save_plot(plot_func, filename):
    plot_func()
    file_path = os.path.join("static", filename)
    plt.savefig(file_path)  # Ensure image is saved correctly
    plt.close()

# Plot functions
def gender_distribution():
    plt.figure(figsize=(5, 5))
    ax = sns.countplot(data=df, x="Gender")
    ax.bar_label(ax.containers[0])
    plt.title("Gender Distribution")

def parent_education_vs_score():
    gb = df.groupby("ParentEduc").agg({"MathScore": "mean", "ReadingScore": "mean", "WritingScore": "mean"})
    plt.figure(figsize=(4, 4))
    sns.heatmap(gb, annot=True)
    plt.title("Parent Education vs Student Score")

def parent_marital_status_vs_score():
    gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore": "mean", "ReadingScore": "mean", "WritingScore": "mean"})
    plt.figure(figsize=(4, 4))
    sns.heatmap(gb1, annot=True)
    plt.title("Parent Marital Status vs Student Score")

def ethnic_group_distribution():
    groups = df["EthnicGroup"].value_counts()
    plt.pie(groups, labels=groups.index, autopct="%1.2f%%")
    plt.title("Ethnic Group Distribution")

def math_score_boxplot():
    sns.boxplot(data=df, x="MathScore")
    plt.title("Math Score Distribution")

def reading_score_boxplot():
    sns.boxplot(data=df, x="ReadingScore")
    plt.title("Reading Score Distribution")

def writing_score_boxplot():
    sns.boxplot(data=df, x="WritingScore")
    plt.title("Writing Score Distribution")

# Saving plots
save_plot(gender_distribution, "gender_distribution.png")
save_plot(parent_education_vs_score, "parent_education_vs_score.png")
save_plot(parent_marital_status_vs_score, "parent_marital_status_vs_score.png")
save_plot(ethnic_group_distribution, "ethnic_group_distribution.png")
save_plot(math_score_boxplot, "math_score.png")
save_plot(reading_score_boxplot, "reading_score.png")
save_plot(writing_score_boxplot, "writing_score.png")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials, please try again!"
    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/graph/<graph_name>')
def show_graph(graph_name):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('graph.html', graph_name=graph_name)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
