from uiautomator2 import connect, device

# Connect to the device
d = connect('your_device_serial_number')  # Replace with your device serial number

# Start the application (replace with your application package name)
app_package = 'com.example.yourapp'
d.app_start(app_package)

# Perform a series of operations in the application, such as clicking buttons, entering text, etc.
d(resourceId="menu_button_id").click()  # Replace with the ID of the button to open the menu
d(resourceId="directory_name_id").click()  # Replace with the ID of the element to modify the directory name

# Simulate device rotation
d.set_orientation("left")  # Replace with the orientation you want to test

# Wait for some time, observe if the application crashes
d.wait(5)  # Adjust the waiting time based on your needs

# Finally, close the application
d.app_stop(app_package)
