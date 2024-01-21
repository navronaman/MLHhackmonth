total_calories = 1000
calorie_counter = 100

total_carbs = 100
carbs_counter = 30

total_sugar = 100
sugar_counter = 10

total_fat = 100
fat_counter = 30

total_fiber = 70
fiber_counter = 40

calorie_percentage = round(calorie_counter/total_calories*100)
sugar_percentage = round(sugar_counter/total_sugar*100)
carbs_percentage = round(carbs_counter/total_carbs*100)
fat_percentage = round(fat_counter/total_fat*100)
fiber_percentage = round(fiber_counter/total_fiber*100)

html_string = '''
<section class = "MainCalorie" id="Calories">
            <h2>Daily Calorie Intake</h2>
            <div class = "container">
                <div class = "calorie"> '''+ str(calorie_percentage)+ '''%</div>
            </div>
            <h3> Calorie Limit: '''+str(total_calories)+'''</h3>
            <h4> Calories Remaining: '''+str(total_calories-calorie_counter)+'''</h4>
        </section>
        <style>
            .MainCalorie h2{
                text-align: center;
            }
            .MainCalorie h3{
                text-align: center;
            }
            .MainCalorie h4{
                text-align: center;
                color: rgb(256,0,0);
            }
            .container{
                background-color: rgb(192, 192, 192); 
                width: 80%; 
                border-radius: 15px; 
            }
            .calorie{
                color: white; 
                padding: 1%; 
                text-align: right; 
                font-size: 20px; 
                border-radius: 15px; 
                background-color: rgb(0, 0, 256); 
                width: ''' + str(calorie_percentage)+ '''%;
            }
        </style>
<title> Other Metrics </title>
        <style>
            #gridSection {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(2, 1fr);
                gap: 10px;
                height: 500px; 
            }
            .quadrant {
                padding: 20px;  
                text-align: center;
            }
            .circProgressSugar::before {
                color: rgb(0,0,256);
                content: "'''+str(sugar_percentage)+'''% \A Total Sugars: '''+str(total_sugar)+'''g \A Sugar Remaining: '''+str(total_sugar-sugar_counter)+'''g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
            .circProgressSugar {
                position: relative;
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 10%;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                  radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                  conic-gradient(blue '''+str(sugar_percentage)+'''%, grey 0);    
              }
              .circProgressCarbs::before {
                color: rgb(0,0,256);
                content: "'''+str(carbs_percentage)+'''% \A Total Carbs: '''+str(total_carbs)+'''g \A Sugar Remaining: '''+str(total_carbs-carbs_counter)+'''g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
              .circProgressCarbs {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                  radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                  conic-gradient(blue '''+str(carbs_percentage)+'''%, grey 0);    
              }
              .circProgressFiber::before {
                color: rgb(0,0,256);
                content: "'''+str(fiber_percentage)+'''% \A Total Fibers: '''+str(total_fiber)+'''g \A Fiber Remaining: '''+str(total_fiber-fiber_counter)+'''g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
              .circProgressFiber {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                  radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                  conic-gradient(blue '''+str(fiber_percentage)+'''%, grey 0);    
              }
              .circProgressFat::before {
                color: rgb(0,0,256);
                content: "'''+str(fat_percentage)+'''% \A Total Fat: '''+str(total_fat)+'''g \A Sugar Remaining: '''+str(total_fat-fat_counter)+'''g";
                display: flex;
                justify-content: center;
                align-items: center;
                position: absolute;
                width:200px;
                height: 200px;
                white-space: pre;
                font-size: 14px;
            }
              .circProgressFat {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-left: 50%;
                margin-top: 50px;
                width: 200px;
                height: 200px;
                border-radius: 50%;
                background: 
                  radial-gradient(closest-side, rgb(255, 255, 255) 79%, transparent 80% 100%),
                  conic-gradient(blue '''+str(fat_percentage)+'''%, grey 0);    
              }
              .quadrant h2{
                margin-left: 20%;
              }
        </style>
        <section id="gridSection">
            <div class="quadrant">
            <h2> Sugar </h2>
                <div class = "circProgressSugar">
                    <progress value = "30" min ="0" max = "100" style="visibility:hidden;height:0;width:0;"></progress>
                </div>
            </div>
            <div class="quadrant">
            <h2> Carbs </h2>
            <div class = "circProgressCarbs">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;"></progress>
                    
                </div>
            </div>
            <div class="quadrant">
            <h2> Fat </h2>
            <div class = "circProgressFat">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;">30%</progress>
                </div>
                </div>
            <div class="quadrant">
            <h2> Fiber </h2>
            <div class = "circProgressFiber">
                    <progress value = "70" min ="0" max = "100" style="visibility:hidden;height:0;width:0;">30%</progress>
                </div>
                </div>
        </section>'''