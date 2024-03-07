# Using Grafana
[Grafana](https://grafana.com/) is a dashboard web application allowing you to visualize data from many different kinds of services and applications. It allows you to visually create dashboards consisting of panels that fetch and possibly process data from sources.
You've all been invited to our grafana instance at https://training.itu.dk:3000/ on your ITU email. If you haven't received anything, please check your spam folder.

In general the workflow is to create a dashboard and then add panels where you then use the Flux Query Language to fetch data (see [Connecting to InfluxDB](Connecting%20to%20InfluxDB.md) for a primer on Flux)


## Creating our first dashboard
First logging in to Grafana you will be presented with the screen below. We will jump straight into it and create a folder do save our dashboards in:

![](images/new_folder.png)

Give it a nice name that identifies your group.
After having done that, we will press the big "New Dashboard" button to get started:

![](images/new_dashboard.png)

Then we will add a panel:

![](images/new_panel.png)

New we get into the panel editor. The top left square is the panel itself, the right square is properties of that panel, like name, description, colours and so on.
The bottom square is the query editor. Here we write the query to fetch that data from InfluxDB we want to show.

Note that there is a sample query button, where you can get some examples to start from. Besides writing a query, you can also press the "transform" tab to change the data from the query before illustrating it. 

Since we just want to show the latest points in my measurement, we will change the dashboard type from "time-series" to "table":

![](images/change_visualization.png)

Next we add a query that just fetches the latest data from the correct measurement:

```
from(bucket: "iot2023")
  |> range(start: v.timeRangeStart, stop:v.timeRangeStop)
  |> filter(fn: (r) =>
    r._measurement == "Kaspers_measurement" and
    r._field == "payload_decoded"
  )
```
Note that we are using the parameters `v.timeRangeStart` and `v.timeRangeStop`. These are provided by Grafana and follow the range set by the drop-down at the top of the panel/dashboard. If you don't see any data it might be because the timerange is too short.

Having written the query, i will also update the panel title and apply. 
Now we can see our beautiful dashboard with its lovely panel in all its glory! To save our dashboard click the floppy-disk/save icon:

![](images/save_dashboard.png)

Make sure to give your dashboard a fitting name, and choose your folder and press save

![](images/saving.png)

Now you can see and find your dashboard in your dashboard folder!

For something a little fancier (but really not much), you can see a dashboard I've created to show latest messages, both by value and by count over time, here: https://training.itu.dk:3000/d/9U-A_BP4z/messages?orgId=6


Now i've written dashboard so much that I am a victim of [semantic satiation](https://en.wikipedia.org/wiki/Semantic_satiation) and need a break. Happy hacking!
