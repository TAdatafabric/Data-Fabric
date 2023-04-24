from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get uploaded file
        uploaded_file = request.files['file']
        
        # Read CSV file into Pandas dataframe
        df = pd.read_csv(uploaded_file)
        
        # Aggregate data using Pandas
        agg_data = df.groupby(['column_to_group_by']).agg({'column_to_aggregate': 'sum'})
        
        # Render template with aggregated data
        return render_template('results.html', tables=[agg_data.to_html(classes='data')], titles=['Aggregated Data'])
    
    # Render file upload form
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
