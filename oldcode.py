from ursina import *
import math

app = Ursina()

# Create a window and set up the 3D camera
window.fullscreen = False
window.title = "Projectile Motion Simulation"
camera.orthographic = True

# Create a root entity to hold the ball, axes, and labels
root = Entity()

# Initial conditions for the projectile motion
initial_position = Vec3(0, 0, 0)  # Set initial position at x=0, y=0, z=0
initial_velocity = Vec3(0, 0, 0)  # Initial velocity (will be updated when the button is clicked)

gravity = Vec3(0, -9.8, 0)  # Gravity in m/s^2
time_step = 0.02

# Initialize the move_ball variable to False
move_ball = False

# Function to update the position of the projectile
def update():
    global initial_position, initial_velocity

    if move_ball:
        # Update the position based on projectile motion equations with gravity
        initial_velocity += gravity * time_step
        initial_position += initial_velocity * time_step
        ball.position = initial_position

# Create a ball entity for the projectile
ball = Entity(parent=root, model='sphere', color=color.orange, scale=0.7)  # Increase the scale of the ball

# Create custom input fields for initial velocity and angle
def create_input_field(parent, position, scale, prompt=''):
    input_field = Entity(parent=parent)
    input_field.text = ''
    input_field.text_entity = Text(parent=input_field, text=prompt, origin=(0, 0), scale=0.05, background=False, y=-0.06)
    input_field.input_text_entity = Text(parent=input_field, text='', origin=(0, 0), scale=0.05, background=True, color=color.dark_gray)
    input_field.input_text_entity.y -= 0.08
    input_field.position = position
    input_field.scale = scale
    input_field.input_active = False

    def input_field_click():
        input_field.input_active = True

    input_field.input_text_entity.on_click = input_field_click

    def input_field_update():
        if input_field.input_active:
            input_field.input_text_entity.text = input_field.text
            if held_keys['backspace']:
                input_field.text = input_field.text[:-1]
            else:
                for key, value in held_keys.items():
                    if key.isalnum():
                        input_field.text += key

    input_field.update = input_field_update

    return input_field

# Create an input field for initial velocity
velocity_input = create_input_field(
    parent=root,
    position=(0.6, 0.45),  # Adjusted position
    scale=(0.2, 0.05),
    prompt='Initial Velocity:'
)

# Create an input field for angle
angle_input = create_input_field(
    parent=root,
    position=(0.6, 0.35),  # Adjusted position
    scale=(0.2, 0.05),
    prompt='Angle (degrees):'
)

# Create a button to start the simulation
def start_simulation():
    global move_ball, initial_velocity

    # Get the input values for initial velocity and angle
    initial_speed = float(velocity_input.input_text_entity.text)
    initial_angle_degrees = float(angle_input.input_text_entity.text)
    initial_angle_radians = math.radians(initial_angle_degrees)

    # Set the initial velocity based on the input values
    initial_velocity = Vec3(initial_speed * math.cos(initial_angle_radians), initial_speed * math.sin(initial_angle_radians), 0)

    # Start the simulation
    move_ball = True

# Create a confirmation button for the input values
confirm_button = Button(text='Start Simulation')
confirm_button.position = (0, 0.2)  # Adjusted position
confirm_button.scale = (0.15, 0.05)
confirm_button.on_click = start_simulation

# Create reference lines for the x and y axes
x_axis = Entity(parent=root, model='cube', color=color.gray, scale=(80, 0.1, 0.1), position=(initial_position.x, 0, 0))
y_axis = Entity(parent=root, model='cube', color=color.gray, scale=(0.1, 40, 0.1), position=(0, initial_position.y, 0))

# Create labels for the x and y axes
label_scale = 25  # Increase the label scale
label_spacing = 3  # Adjust the spacing between the labels
for i in range(-20, 21):
    if i != 0:
        # Create x-axis label
        label_x = Text(str(i), origin=(0, 0), scale=label_scale, background=False)
        label_x.x = i * label_spacing
        label_x.y = -0.5
        label_x.parent = root

        # Create y-axis label
        label_y = Text(str(i), origin=(0, 0), scale=label_scale, background=False)
        label_y.x = -0.5
        label_y.y = i * label_spacing
        label_y.parent = root

# Run the Ursina app
app.run()
