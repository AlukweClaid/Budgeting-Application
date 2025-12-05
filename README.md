# Budgeting App
Its a tool designed to help one keep track of their financial expenditure and help in making better financial decisions according to the generated reports and data on the various earnings of the user of the application
# steps to achieving the tool
 - Firstly I ensured the first instance of the App is running
  after following the correct procedures to install Django
  - Created a new Django project named Budgetingproject
  - Created a new Django app named BudgetingApp
  - Added the BudgetingApp to the INSTALLED_APPS list in settings.py
  - Configured the templates directory in settings.py to include a custom directory for HTML files
  - Created a simple view in views.py of BudgetingApp that returns a welcome message
  - Mapped the view to a URL in urls.py of BudgetingApp and included it in the main project's urls.py
  - Created a base HTML template in the templates directory and extended it in a home.html file
  - Ran the development server and accessed the home page to see the welcome message displayed correctly
  - Next, I created models for BudgetItem, Category, and Transaction in models.py of BudgetingApp
  - Made migrations and migrated the database to create the necessary tables
  - Registered the models in admin.py to manage them via Django admin interface
  - Created views for listing, creating, updating, and deleting BudgetItems, Categories, and Transactions using Django's generic class-based views
  - Created corresponding HTML templates for each view, extending the base template
  - Configured URLs for each view in urls.py of BudgetingApp and included them in the main project's urls.py
  - Added Bootstrap CSS framework to the base template for styling
  - Tested each functionality by running the development server and interacting with the web application
  - Finally, I committed the changes to a Git repository to track the development progress.
# Authentication
 - Implemented user authentication features in the BudgetingApp
  - Created custom views for user login, logout, and registration in views.py of BudgetingApp
  - Used Django's built-in authentication views and forms to handle user authentication
  - Created HTML templates for login, logout, and registration pages, extending the base template
  - Configured URLs for authentication views in urls.py of BudgetingApp and included them in the main project's urls.py
  - Updated settings.py to include LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, and LOGIN_URL for proper redirection after login/logout
  - Ensured that certain views (like creating or editing BudgetItems) are restricted to authenticated users only using Django's @login_required decorator or LoginRequiredMixin
  - Tested the authentication features by registering a new user, logging in, accessing restricted pages, and logging out
  - Committed the authentication feature changes to the Git repository.

## Payments integration (M-Pesa)
  - Integrated M-Pesa payment gateway into the BudgetingApp
    - Created a new view in views.py of BudgetingApp to handle M-Pesa payment initiation
    - Used M-Pesa API to set up payment requests and handle responses
    - Created an HTML template for the payment page, extending the base template
    - Configured URLs for the payment view in urls.py of BudgetingApp and included them in the main project's urls.py
    - Added necessary settings in settings.py for M-Pesa API credentials and endpoints
    - Tested the M-Pesa payment integration by initiating a payment request and verifying the response
    - Handled success and failure responses appropriately in the application
    - Committed the M-Pesa integration changes to the Git repository.
# end


