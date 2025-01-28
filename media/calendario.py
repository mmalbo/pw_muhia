<div class="calendar">
          <div class="container">
            <header class="text-center text-white">
              <h4 class="display-8">Calendario</h4>
            </header>
            <!-- Calendar -->
            {{ html_cal|safe }}
              <style>
                .calendar {
                  width: 100%;
                  margin: auto;
                  font-size: 14px;
                }
                .calendar tr, .calendar td {
                  border: 1px solid black;
                }
                .calendar th {
                  padding: 5px;
                  text-align: center;                            
                  font-variant-caps: all-small-caps;
                  font-family: "Lora", "serif";
                  font-size: 18px;
                  background-color: lightblue;
                }
                .calendar th.month{
                  font-size: 36px;
                  background-color: var(--blue);
                }
                .calendar td {
                  width: 10%;
                  text-align: center;
                  height: 5%;
                  padding: 5px 0px 0px 5px;
                }
                #calendar td.calendar.date.today {
                  background-color: var(--blue);
                }
                ul {
                  height: 100%;
                  padding: 0px 5px 0px 20px;
                }
                a {
                  color: #17a2b8;
                }
              </style>
          </div>
        </div>