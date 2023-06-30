```python
from flask import render_template, redirect, url_for, flash, request
from webapp import app, db
from webapp.forms import SearchForm, CostEstimateForm
from webapp.patent_search import search_patent
from webapp.cost_estimator import estimate_cost
from webapp.models import Patent, CostEstimate

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        patent = search_patent(form.patent.data)
        if patent:
            flash('searchSuccess', 'success')
            return redirect(url_for('results', patent_id=patent.id))
        else:
            flash('searchFailure', 'danger')
    return render_template('index.html', form=form)

@app.route('/results/<int:patent_id>', methods=['GET'])
def results(patent_id):
    patent = Patent.query.get(patent_id)
    if patent:
        return render_template('results.html', patent=patent)
    else:
        return render_template('error.html', message='Patent not found')

@app.route('/cost_estimate', methods=['GET', 'POST'])
def cost_estimate():
    form = CostEstimateForm()
    if form.validate_on_submit():
        cost_estimate = estimate_cost(form.patent.data)
        if cost_estimate:
            flash('estimateSuccess', 'success')
            return render_template('cost_estimate.html', cost_estimate=cost_estimate)
        else:
            flash('estimateFailure', 'danger')
            return redirect(url_for('index'))
    return render_template('cost_estimate.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message='Page not found'), 404
```