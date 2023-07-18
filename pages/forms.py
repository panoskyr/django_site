from django import forms 

class ContactForm(forms.Form):

	yourname=forms.CharField(
			max_length=80,
			label='Your Name',widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Name',
			'required data-validation-required-message':"Please enter your name.",
			})

		)
	youremail=forms.EmailField(
		required=False, 
		label='Your email',
		widget=forms.EmailInput(
			attrs={
			'class':'form-control',
			'placeholder':'Email Address',
			'required data-validation-required-message':"Please enter your email address.",
			})
		)
	yoursubject=forms.CharField(max_length=100, 
			label='Subject',
			widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Subject',
			'required data-validation-required-message':"Please enter a message subject.",
			})
			)
	yourmessage=forms.CharField(max_length=100, 
			label='Message',
			widget=forms.TextInput(
			attrs={
			'class':'form-control',
			'placeholder':'Message',
			'required data-validation-required-message':"Please enter a message.",
			})
			)
