from django.test import TestCase
from .forms import ContactForm
# Create your tests here.
class TestContactForm(TestCase): 
    
    def test_form_is_valid(self):  
        form=ContactForm({
            'name':'Jane', 
            'email':'jane@example.com', 
            'phone':'123345'
        }) 
        
        self.assertTrue(form.is_valid())
    
    def test_name_is_required(self):  
        form=ContactForm({
            
            'email':'jane@example.com', 
            'phone':'123345'
        }) 
        
        self.assertFalse(form.is_valid())
     
    def test_email_is_required(self):  
        form=ContactForm({
            'name':'Jane', 
            'phone':'123456789'
        }) 
        
        self.assertFalse(form.is_valid()) 
        
        
    def test_phone_is_required(self):  
        form=ContactForm({
            'name':'Jane', 
            'email':'jane@example.com', 
            
        }) 
        
        self.assertFalse(form.is_valid()) 
    
     