# Humidity

    from(bucket: "iot2024_final")
      |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
      |> filter(fn: (r) => r["_measurement"] == "bjornars_measurement")
      |> filter(fn: (r) => r["_field"] == "humidity")
      |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
      |> yield(name: "mean")

# Temperature

    from(bucket: "iot2024_final")
      |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
      |> filter(fn: (r) => r["_measurement"] == "bjornars_measurement")
      |> filter(fn: (r) => r["_field"] == "temperature")
      |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
      |> yield(name: "mean")

# CO2

    from(bucket: "iot2024_final")
      |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
      |> filter(fn: (r) => r["_measurement"] == "bjornars_measurement")
      |> filter(fn: (r) => r["_field"] == "co2")
      |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)
      |> yield(name: "mean")