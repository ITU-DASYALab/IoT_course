# Checklist for nodes on balloon mission


## Wiring

- everything is soldered properly - no breadboards or other unstable connections 
- if the sensor needs to be outside the enclosure box (.e.g for air quality or light), sensor is connecetd via wires minimum 20 cm in length

## Power

- can run on one battery (18650) for a minimum of 5 hours

- 
## Timing

- do we comply with duty cycle

## Data flow

- consider how your data gets to the backend - webhook? py script?

-- if py script, remember that you have to have this running during the experiment

## Testing

- tested to be able to send data to TTN gateways, preferrably also over long distance (> 40 km)

- data arrives at backend 

- 
