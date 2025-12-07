# Budgeting App
Its a tool designed to help one keep track of their financial expenditure and help in making better financial decisions according to the generated reports and data on the various earnings of the user of the application
# About the Tool
- I like to think of the tool as something that can be incorporated in financial institution apps such as an Mpesa or bank applications that can help to achieve financial literacy and nice financial budgeting since on the financial apps is where the transactions take place on a full time basis
# Purose of the app
- It is designed to help individuals not misappropriate the funds and with various updates it helps one be able to not miss payments of urgent stuff such as rent due to bad financial decisions which has proved to be a great problem with the current generation hence its a useful tool to help one not miss important deadlines on various payments and when one decides to acquire loans on the financial instituitions apps they atleast have a clear road map on where to spend and help to avoid getting loans and repaying a loan that was never useful to the individual and it curbs issues such as financial addictions such as gambling since with proper budgeting and financial allocation one gets to achieve alot in terms of financial growth.
# Solution it solves 
- With proper funds allocation and implementation the economic development of a nation is guaranteed since one can only get into necessary debt not unnecessary since it brings about proper financial decisions and one cannot have regrets on taking some loans and it helps since it eases repayment of loans since one doesn't feel a burden because the loans they take had a proper plan for implementation hence solving such a problem also takes care of ones financial well being thus a happy individual leads to a happy economy.  
# Steps to achieving the tool
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



