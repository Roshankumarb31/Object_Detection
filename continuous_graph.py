# import streamlit as st
# import pandas as pd
# import numpy as np

# # Generate some example data
# data = pd.DataFrame({
#     'x': np.arange(100),
#     'y': np.random.randn(100)
# })

# # Title and description
# st.title('Continuous Line Graph Example')
# st.write('This is a continuous line graph with random data.')

# # Display the line chart
# st.line_chart(data.set_index('x'))




# import streamlit as st
# import pandas as pd
# import numpy as np
# import time
# import altair as alt

# data = pd.DataFrame(columns=['x', 'y'])

# chart_container = st.empty()

# for i in range(100):
    
#     y_value = np.sin(i / 10)
    
#     new_data = pd.DataFrame({'x': [i], 'y': [y_value]})
#     data = data.append(new_data, ignore_index=True)
    
#     color = 'red' if y_value > 0.5 else 'blue'
    
#     chart = alt.Chart(data).mark_line(color=color).encode(x='x', y='y')
#     chart_container.altair_chart(chart, use_container_width=True)
    
#     time.sleep(0.1)



import numpy as np
import pandas as pd
import streamlit as st
import time
import altair as alt

st.title('Continuous Graph:)')
data = pd.DataFrame(columns=['x', 'y'])

chart_container = st.empty()

num_data_points = 10
i = 0

while True:
    
    y_value = np.random.randint(1,11)
    
    new_data = pd.DataFrame({'x': [i], 'y': [y_value]})
    data = pd.concat([data, new_data], ignore_index=True)
    
    colors_list = [['rgba(55, 0, 0)','rgba(121, 0, 0)','rgba(187, 0, 0)','rgba(255, 0, 0)', 'red'], 
                ['rgba(0, 38, 52)','rgba(0, 84, 114)','rgba(0, 129, 176)','rgba(0, 176, 240)', 'rgba(0, 176, 240)']]
    
    color = colors_list[0] if y_value > 5 else colors_list[1]
    
    gradient = alt.Gradient(
        gradient='linear',
        stops=[
            alt.GradientStop(color = 'black', offset = 0),  
            alt.GradientStop(color = color[0], offset = 0.25),
            alt.GradientStop(color = color[1], offset = 0.5),
            alt.GradientStop(color = color[2], offset = 0.75),
            alt.GradientStop(color = color[3], offset = 1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
    
    chart = alt.Chart(data).mark_area(
        line = {'color': color[4]},
        color = gradient
    ).encode(x = 'x', y = alt.Y('y', scale = alt.Scale(domain = [0, 10])))
    
    data = data.tail(num_data_points)
    
    # Display the Altair chart
    chart_container.altair_chart(chart, use_container_width = True)
    
    
    time.sleep(0.5)
    
    i += 1