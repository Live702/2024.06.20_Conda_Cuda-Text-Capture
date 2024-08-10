import cv2
import numpy as np
import pyautogui
import isaacsim  # Assuming you have Isaac Sim installed

# --- Isaac Sim Environment Setup ---

import omni.isaac.core.utils.stage as stage_utils
import omni.isaac.core.utils.nucleus as nucleus_utils
from pxr import UsdGeom
from omni.isaac.core.utils.prims import create_prim

# Create a new stage
stage = stage_utils.get_current_stage()
stage_units = UsdGeom.GetStageMetersPerUnit(stage)

# Add a flat ground plane
ground_plane = create_prim(

    prim_path="/World/ground_plane",
    prim_type="Plane",
    position=(0, 0, 0),  # Centered at the origin
    rotation=(0, 0, 0),
    scale=(100, 100, 1),  # Adjust size as needed
)
UsdGeom.Mesh(ground_plane).CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)  # Disable tessellation
# Set up the material
material_path = nucleus_utils.get_assets_root_path() + "/Isaac/Materials/Ground/default_ground.material"
nucleus_utils.add_reference_to_prim(ground_plane.GetPath(), material_path)

# Add a camera prim
camera = create_prim(
    prim_path="/World/Camera",
    prim_type="Camera",
    position=(0, 0, 6 / stage_units),  # 6 feet above the ground
    rotation=(0, -90, 0),  # Rotated -90 degrees around the X-axis 
)

# Set camera as the viewport camera
stage_utils.set_active_camera("/World/Camera")
# --- End of Isaac Sim Setup ---


# Initialize Isaac Sim
sim = isaacsim.SimulationApp()

# Load your game scene (replace with your actual path)
#sim.load_scene("your_game_scene.usd")  # Replace with your game scene file

# Get the window handle for PyAutoGUI (you may need to adjust the window title)
window_title = "overwatch"  # Replace with the actual title of your Isaac Sim window
window = pyautogui.getWindowsWithTitle(window_title)[0]

# Define the region of the game window you want to capture (adjust as needed)
left = window.left
top = window.top
width = window.width
height = window.height

# Object detection logic (replace with your actual implementation)
def detect_red_objects(frame):
    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color range
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a mask for red pixels
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Find contours of red objects
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

# Main loop
while True:
    if not window.isActive:  # Check if window is still active
        print(f"Window '{window_title}' closed. Exiting...")
        break  # Exit loop if window is closed

    # Capture screenshot of the game window
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    # Convert screenshot to OpenCV format (numpy array)
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Object detection
    red_contours = detect_red_objects(frame)

    # Draw bounding boxes around detected objects
    for contour in red_contours:
        # Calculate bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle

    # Display the frame with detected objects
    cv2.imshow("Game Window with Detection", frame)

    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
