# Little Lemon API Project

### Suggested endpoints for testing (with _Insomnia_):
1. **View index page:** /restaurant/ (GET)

2. **Register user:** /auth/users/ (GET then POST)
   **if using _Insomnia_, select Multipart Form from Body tab and add 'email', 'username', 'password' as names**

3. **Copy token:** /auth/token/login/ (GET)
   **in _Insomnia_, now select Bearer Token from Auth tab and paste in your token**

5. **Book a table:** /restaurant/booking/ (GET then POST)
   **select Multipart Form from Body tab use 'name', 'no_of_guests', 'booking_date' as names (remember to input your values)**

6. **Browse the menu:** /api/menu-items/ (GET)

7. **Log out feeling happy and content:** /auth/token/logout/ (POST)
