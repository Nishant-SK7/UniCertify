
        const roleSelect = document.getElementById('role');
        const formFields = document.getElementById('formFields');
        const userIdLabel = document.getElementById('userIdLabel');
        const departmentGroup = document.getElementById('departmentGroup');
        const signupForm = document.getElementById('signupForm');
        const errorMessage = document.getElementById('errorMessage');
        const successMessage = document.getElementById('successMessage');

        roleSelect.addEventListener('change', function() {
            const selectedRole = this.value;
            
            if (selectedRole) {
                formFields.classList.remove('hidden');
                formFields.classList.add('fade-in');
                
                if (selectedRole === 'admin') {
                    userIdLabel.textContent = 'Admin ID';
                    departmentGroup.classList.add('hidden');
                    document.getElementById('department').required = false;
                } else {
                    userIdLabel.textContent = 'Student ID';
                    departmentGroup.classList.remove('hidden');
                    document.getElementById('department').required = true;
                }
            } else {
                formFields.classList.add('hidden');
            }
        });
