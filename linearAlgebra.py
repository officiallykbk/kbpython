# import numpy as np
# import matplotlib.pyplot as plt
# import math

# # Original points of the polygon
# n=int(input("Enter number of vertices in the polygon: "))
# while n<3:
#     n=int(input("Error!Vertice must be 3 or more\n Enter the correct number of vertices."))
               
# inputedarray=[]
# print("Enter coordinates (x, y) for each vertex:")
# for i in range(n):
#     x = float(input(f"Enter the x-coordinate{i+1}: "))
#     y = float(input(f"Enter the y-coordinate{i+1}: "))
#     inputedarray.append([x,y])
# points = np.array(inputedarray)

# print(f"Points of original polygon: {points}")

# def translate():
#     global translation
#     tx=float(input("How far do you want to translate on the x axis: "))
#     ty=float(input("How far do you want to translate on the y axis: "))
#     translation = np.array([[1, 0, tx],
#     [0, 1, ty],
#     [0, 0, 1]])

# def rotate():
#     global rotation
#     Rotationangle=math.radians(float(input("What is your angle of rotation: ")))
#     rotation = np.array([[np.cos(Rotationangle), -np.sin(Rotationangle), 0],
#     [np.sin(Rotationangle), np.cos(Rotationangle), 0],
#     [0, 0, 1]])

    
# def scale():
#     global scaling
#     Sx=float(input("Enter scaling factor in the x-axis, either positively or negatively: "))
#     Sy=float(input("Enter scaling factor in the y-axis, either positively or negatively: "))
#     scaling = np.array([[Sx, 0, 0],
#     [0, Sy, 0],
#     [0, 0, 1]])

    

# print("""What action do you want to apply to your polygon\nTranslation(T), Rotation(R),Scale(S)\n
#       Pick any of the abbreviation or if you want perform multiple actions put the
#       abbreviations together eg. TR or RT or TRS""")

# action=str(input("")).upper()
# if(action=="S"):
#     scale()
#     scaled_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         scaled_points.append(np.dot(scaling, augmented_point)[:2])
#     finalPoints=np.array(scaled_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="T"):
#     translate()
#     translated_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         translated_points.append(np.dot(translation, augmented_point)[:2])
#     finalPoints=np.array(translated_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="R"):
#     rotate()
#     rotated_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         rotated_points.append(np.dot(rotation, augmented_point)[:2])
#     finalPoints=np.array(rotated_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="TR"):
#     translate()
#     rotate()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(rotation, augmented_point) 
#         transformed_point=np.dot(translation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="RT"):
#     translate()
#     rotate()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(translation, augmented_point) 
#         transformed_point=np.dot(rotation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="SR"):
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(rotation, augmented_point) 
#         transformed_point=np.dot(scaling, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="ST"):
#     translate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(translation, augmented_point) 
#         transformed_point=np.dot(scaling, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="TS"):
#     translate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(scaling, augmented_point) 
#         transformed_point=np.dot(translation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="RS"):
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1)
#         transformed_point = np.dot(scaling, augmented_point) 
#         transformed_point=np.dot(rotation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="RTS"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(rotation, augmented_point)
#         transformed_point = np.dot(translation, transformed_point)
#         transformed_point = np.dot(scaling, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="SRT"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(scaling, augmented_point)
#         transformed_point = np.dot(rotation, transformed_point)
#         transformed_point = np.dot(translation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="TRS"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(translation, augmented_point)
#         transformed_point = np.dot(rotation, transformed_point)
#         transformed_point = np.dot(scaling, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="STR"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(scaling, augmented_point)
#         transformed_point = np.dot(translation, transformed_point)
#         transformed_point = np.dot(rotation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="TSR"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(translation, augmented_point)
#         transformed_point = np.dot(scaling, transformed_point)
#         transformed_point = np.dot(rotation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
# elif(action=="RST"):
#     translate()
#     rotate()
#     scale()
#     transformed_points = []
#     for point in points:
#         augmented_point = np.append(point, 1) 
#         transformed_point = np.dot(rotation, augmented_point)
#         transformed_point = np.dot(scaling, transformed_point)
#         transformed_point = np.dot(translation, transformed_point)
#         transformed_points.append(transformed_point[:2])
#     finalPoints=np.array(transformed_points)
#     print(f"Transformed points\n{finalPoints}")
    
        
# # Plotting
# finalPointClosed = np.vstack((finalPoints, finalPoints[0]))  
# pointsClosed = np.vstack((points, points[0])) 
# plt.plot(pointsClosed[:, 0], pointsClosed[:, 1], 'bo-', label='Original Polygon')
# plt.plot(finalPointClosed[:, 0], finalPointClosed[:, 1], 'ro-', label='Transformed Polygon')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('2D Polygon Transformation')
# plt.axis('equal')
# plt.legend()
# plt.grid(True)
# plt.show()

    
import numpy as np
import matplotlib.pyplot as plt
import math

# Function to get user input for translation
def get_translation():
    tx = float(input("Enter the translation in the x-axis: "))
    ty = float(input("Enter the translation in the y-axis: "))
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

# Function to get user input for rotation
def get_rotation():
    angle = math.radians(float(input("Enter the angle of rotation in degrees: ")))
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                     [np.sin(angle), np.cos(angle), 0],
                     [0, 0, 1]])

# Function to get user input for scaling
def get_scaling():
    sx = float(input("Enter the scaling factor in the x-axis: "))
    sy = float(input("Enter the scaling factor in the y-axis: "))
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

# Function to get user input for reflection
def get_reflection():
    axis = input("Enter the axis for reflection (X or Y): ").upper()
    if axis == "X":
        return np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, 1]])
    elif axis == "Y":
        return np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])

# Function to get user input for shearing
def get_shearing():
    shear_x = float(input("Enter the shearing factor in the x-axis: "))
    shear_y = float(input("Enter the shearing factor in the y-axis: "))
    return np.array([[1, shear_x, 0],
                     [shear_y, 1, 0],
                     [0, 0, 1]])

# Function to apply transformations
def apply_transformations(points, transformations):
    transformed_points = []
    for point in points:
        augmented_point = np.append(point, 1)
        transformed_point = augmented_point
        for transformation in transformations:
            transformed_point = np.dot(transformation, transformed_point)
            transformed_points.append(transformed_point[:2])
    return np.array(transformed_points)

# Function to plot polygons
def plot_polygons(original_points, transformed_points):
    original_points_closed = np.vstack((original_points, original_points[0]))
    transformed_points_closed = np.vstack((transformed_points, transformed_points[0]))
    plt.plot(original_points_closed[:, 0], original_points_closed[:, 1], 'bo-', label='Original Polygon')
    plt.plot(transformed_points_closed[:, 0], transformed_points_closed[:, 1], 'ro-', label='Transformed Polygon')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('2D Polygon Transformation')
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()


# Main program
n=int(input("Enter number of vertices in the polygon: "))
while n<3:
    n=int(input("Error!Vertice must be 3 or more\n Enter the correct number of vertices."))
               
inputedarray=[]
print("Enter coordinates (x, y) for each vertex:")
for i in range(n):
    x = float(input(f"Enter the x-coordinate{i+1}: "))
    y = float(input(f"Enter the y-coordinate{i+1}: "))
    inputedarray.append([x,y])
points = np.array(inputedarray)

cont="y"
while cont=="y":
    print(f"Points of original polygon: {points}")
    # Get user input for transformations
    transformations = []
    actions = input("Enter the sequence of transformations (T for Translation, R for Rotation, S for Scaling, F for Reflection, H for Shearing): ").upper()
    options=['T','R','S','F','H']
    while actions not in options:
        print("You can only enter T(translate) or R(rotate) or S(scale) or F(reflect) or H(shear) ")
        actions = input("Enter the sequence of transformations (T for Translation, R for Rotation, S for Scaling, F for Reflection, H for Shearing): ").upper()
        
    for action in actions:
        if action == "T":
            transformations.append(get_translation())
        elif action == "R":
            transformations.append(get_rotation())
        elif action == "S":
            transformations.append(get_scaling())
        elif action == "F":
            transformations.append(get_reflection())
        elif action == "H":
            transformations.append(get_shearing())

    # Apply transformations
    transformed_points = apply_transformations(points, transformations)
    print(f"Transformed points:\n{transformed_points}")

    # Plot polygons
    plot_polygons(np.array(points), transformed_points)
    points=transformed_points
    cont=str(input("Do you want to continue(y/n): ")).lower()
    while cont!="y" and cont!="n":
        cont=str(input("Do you want to continue transforming(y/n): ")).lower()