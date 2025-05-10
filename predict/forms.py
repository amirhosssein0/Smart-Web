from django import forms

class PredictForm(forms.Form):
    bedrooms = forms.IntegerField(min_value=0, max_value=15, label="Bedroom")
    sqft_living = forms.IntegerField(min_value=300, max_value=15000, label="Living sqft")
    sqft_lot = forms.IntegerField(min_value=500, max_value=2000000, label="Land Area")
    floors = forms.FloatField(min_value=1.0, max_value=3.5, label="Floors")
    waterfront = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Waterfront")
    yr_built = forms.IntegerField(min_value=1934, max_value=2014, label="Built Year")
    sqft_above = forms.IntegerField(min_value=0, max_value=15000, label="Upper Floors sqft")
    sqft_basement = forms.IntegerField(min_value=0, max_value=5000, label="Lower Floors sqft")
    grade = forms.ChoiceField(
        choices=[(i, f"Grade {i}") for i in range(1, 14)],
        label="Built Score"
    )
    view = forms.ChoiceField(
        choices=[(i, f"view {i}") for i in range(0, 5)],
        label="View"
    )
    condition = forms.ChoiceField(
        choices=[(i, f"stat {i}") for i in range(1, 6)],
        label="Status"
    )
    house_renovated = forms.ChoiceField(choices=[(0, 'No'), (1, 'Yes')], label="Repare")
    long = forms.FloatField(min_value=-122.5, max_value=-121.3, label="Long")
    lat = forms.FloatField(min_value=47.1, max_value=47.8, label="Lat")
