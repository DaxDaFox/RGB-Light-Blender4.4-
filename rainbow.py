import bpy

light_obj = bpy.data.objects["Area"]  
light_data = light_obj.data

def add_color_driver(index, expression):  
    fcu = light_data.driver_add("color", index)  
    driver = fcu.driver  
    driver.type = 'SCRIPTED'  
    driver.expression = expression

    var = driver.variables.new()  
    var.name = "var"  
    var.type = 'SINGLE_PROP'  
    target = var.targets[0]  
    target.id_type = 'SCENE'  
    target.id = bpy.context.scene  
    target.data_path = "frame_current"

add_color_driver(0, "0.5 + 0.5 * sin(var * 0.3)")
add_color_driver(1, "0.5 + 0.5 * sin(var * 0.39)") 
add_color_driver(2, "0.5 + 0.5 * sin(var * 0.51)")
