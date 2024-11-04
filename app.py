from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    budget = float(request.form.get('budget'))
    frequency_cap = int(request.form.get('frequency_cap'))
    kpi_target = request.form.get('kpi_target')

    simulation_results = run_simulation(budget, frequency_cap, kpi_target)
    return jsonify(simulation_results)

import random

def run_simulation(budget, frequency_cap, kpi_target):
    # Simulate some basic results based on the inputs
    
    # Generate mock results
    impressions = int(budget * (random.uniform(1.0, 1.5))) 
    click_through_rate = random.uniform(0.01, 0.1) * (frequency_cap / 10)
    cost_per_conversion = budget / (impressions * click_through_rate * 10 + 1) 

    # Adjust results based on KPI target
    if kpi_target == "CPM":  
        cpm = (budget / impressions) * 1000
        return {
            'kpi': 'CPM',
            'value': round(cpm, 2),
            'impressions': impressions,
            'click_through_rate': round(click_through_rate * 100, 2),
            'cost_per_conversion': round(cost_per_conversion, 2)
        }
    elif kpi_target == "CTR":  # Click-through rate
        return {
            'kpi': 'CTR',
            'value': round(click_through_rate * 100, 2),
            'impressions': impressions,
            'click_through_rate': round(click_through_rate * 100, 2),
            'cost_per_conversion': round(cost_per_conversion, 2)
        }
    elif kpi_target == "CPC":  # Cost per conversion
        return {
            'kpi': 'CPC',
            'value': round(cost_per_conversion, 2),
            'impressions': impressions,
            'click_through_rate': round(click_through_rate * 100, 2),
            'cost_per_conversion': round(cost_per_conversion, 2)
        }
    else:
        return {
            'error': 'Invalid KPI target'
        }


if __name__ == '__main__':
    app.run(debug=True)