// Forms Handling
const GOOGLE_SCRIPT_URL = "";

document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('form');

  forms.forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      
      const submitBtn = form.querySelector('button[type="submit"]');
      const statusDiv = form.querySelector('.form-status');
      
      if (!validateForm(form)) {
        return;
      }
      
      // Update UI for loading state
      const originalBtnText = submitBtn.innerHTML;
      submitBtn.innerHTML = 'Submitting...';
      submitBtn.disabled = true;
      if (statusDiv) {
        statusDiv.className = 'form-status loading';
        statusDiv.textContent = 'Sending your request...';
        statusDiv.style.display = 'block';
      }

      try {
        if (GOOGLE_SCRIPT_URL) {
          const formData = new FormData(form);
          // Example of how it would be connected later:
          /*
          const response = await fetch(GOOGLE_SCRIPT_URL, {
            method: 'POST',
            body: formData
          });
          if (!response.ok) throw new Error('Network response was not ok');
          */
          
          // Simulate network request for now since URL is empty
          await new Promise(resolve => setTimeout(resolve, 1000));
        } else {
          // Placeholder behavior
          await new Promise(resolve => setTimeout(resolve, 1000));
        }

        // Success state
        if (statusDiv) {
          statusDiv.className = 'form-status success';
          statusDiv.textContent = 'Thank you. Your request has been received.';
        }
        form.reset();
      } catch (error) {
        // Error state
        if (statusDiv) {
          statusDiv.className = 'form-status error';
          statusDiv.textContent = 'There was an error submitting your request. Please try again later.';
        }
        console.error('Form submission error:', error);
      } finally {
        submitBtn.innerHTML = originalBtnText;
        submitBtn.disabled = false;
        
        // Hide status message after 5 seconds
        if (statusDiv) {
          setTimeout(() => {
            statusDiv.style.display = 'none';
          }, 5000);
        }
      }
    });
  });
});

function validateForm(form) {
  let isValid = true;
  const requiredInputs = form.querySelectorAll('[required]');
  
  // Remove existing error states
  form.querySelectorAll('.error-message').forEach(el => el.remove());
  form.querySelectorAll('.error-border').forEach(el => el.classList.remove('error-border'));
  
  requiredInputs.forEach(input => {
    if (!input.value.trim()) {
      isValid = false;
      showError(input, 'This field is required');
    } else if (input.type === 'email' && !isValidEmail(input.value)) {
      isValid = false;
      showError(input, 'Please enter a valid email address');
    }
  });
  
  return isValid;
}

function isValidEmail(email) {
  const re = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  return re.test(email);
}

function showError(input, message) {
  input.classList.add('error-border');
  input.style.borderColor = '#991b1b';
  const errorDiv = document.createElement('div');
  errorDiv.className = 'error-message';
  errorDiv.style.color = '#991b1b';
  errorDiv.style.fontSize = '0.875rem';
  errorDiv.style.marginTop = '0.25rem';
  errorDiv.textContent = message;
  input.parentNode.appendChild(errorDiv);
  
  // Reset border on input
  input.addEventListener('input', function() {
    input.style.borderColor = 'var(--border)';
    if (input.parentNode.querySelector('.error-message')) {
      input.parentNode.querySelector('.error-message').remove();
    }
  }, { once: true });
}
