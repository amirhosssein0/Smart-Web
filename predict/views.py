from django.shortcuts import render
from .forms import PredictForm
import joblib
import os
import numpy as np

from django.views import View

class PredictView(View):
    template_name = 'predict/form.html'

    def get(self, request):
        form = PredictForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PredictForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data

            data = [
                int(cleaned['bedrooms']),
                int(cleaned['sqft_living']),
                int(cleaned['sqft_lot']),
                float(cleaned['floors']),
                int(cleaned['waterfront']),
                int(cleaned['yr_built']),
                int(cleaned['sqft_above']),
                int(cleaned['sqft_basement']),
                int(cleaned['grade']),
                int(cleaned['view']),
                int(cleaned['condition']),
                int(cleaned['house_renovated']),
                float(cleaned['long']),
                float(cleaned['lat']),
            ]

            model_path = os.path.join('predict', 'ml_model', 'best_model.pkl')
            model = joblib.load(model_path)
            prediction = model.predict(np.array(data).reshape(1, -1))[0]

            context = {
                'prediction': int(prediction),
            }
            return render(request, 'predict/result.html', context)

        return render(request, self.template_name, {'form': form})

