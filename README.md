# Test Case

## Parts

- Web Service for displaying polygons from the DB in the browser
- Polygon optimization

## Tools used

- Python
- Django
- PostgreSQL
- LeafletJS

### Why not Flask?

Because there were already a couple of things I needed to learn first (PostGIS, LeafletJS) and thus I didn't want to
spend extra time to freshen my Flask knowledge (it is a little rusty since I haven't used it in a long time).

## Optimization algorithm
It is pretty straight forward:

It iterates through all restaurants and when it finds a restaurant that overlaps with another it will first find the best
direction to move the restaurant. It does it by moving the restaurant in different directions and comparing the resulting overlapping area.
The direction with the least amount of overlapping area is considered the best direction. After finding the best direction to move the
restaurant it will move the restaurant in that direction until there is no overlapping area between the restaurants.

As the algorithm does not change the shape of the polygon but simply translates it, the area will not change.

## Setting up

```
docker-compose up
```

## Usage

1. Create restaurants by sending requests to the relevant endpoint as shown in the [API Endpoints section].
2. Go to `http://localhost:8000`.
3. You will see the restaurants on the map with their delivery areas: http://take.ms/cT3Pj
4. Click on the `Optimize` button on the bottom. The page will refresh after optimization is done.
5. You will see the restaurants with new delivery areas optimized not to overlap with each other: http://take.ms/ZF1DJ

## Running the tests

```
docker-compose exec web pytest
```

## Notes

1. The optimization algorithm may not be what is needed if different business rules are taken into account. As this is
a test case, I assumed that there is no constraint in how far can the polygon move from its original location.
2. The `translate()` function could be improved by using some library instead of the db function that is used here. It would
improve the readability as well.
3. Dockerfile could further be improved by using smaller base images such as alpine.

## API Endpoints

1. Create a restaurant: `POST` to `/restaurants/` with the following data:

```
{
	"name": "KFC",
	"location": {"type": "Point", "coordinates":  [52.5247258, 13.39303289999998]},
	"delivery_area": {"type":"Polygon","coordinates":[[[13.39303289999998,52.5337089528412],[13.395913937206183,52.53353630910886],[13.39868419197304,52.533025016495436],[13.401237149192186,52.53219473502801],[13.403474662897601,52.53107738892567],[13.405310733632021,52.529715937184704],[13.406674815342607,52.528162719640235],[13.407514524422746,52.5264774425287],[13.40779764710031,52.52472488142933],[13.407513368897478,52.522972390251994],[13.406672680210292,52.521287312261535],[13.405307943947166,52.519734392722825],[13.40347164336441,52.51837329250363],[13.401234359507212,52.517256297923076],[13.398682056840562,52.516426314461434],[13.3959127816808,52.51591522096912],[13.39303289999998,52.51574264715881],[13.390153018319161,52.51591522096912],[13.387383743159399,52.516426314461434],[13.384831440492748,52.517256297923076],[13.38259415663555,52.51837329250363],[13.380757856052794,52.519734392722825],[13.37939311978967,52.521287312261535],[13.378552431102484,52.522972390251994],[13.37826815289965,52.52472488142933],[13.378551275577214,52.5264774425287],[13.379390984657354,52.528162719640235],[13.38075506636794,52.529715937184704],[13.382591137102361,52.53107738892567],[13.384828650807776,52.53219473502801],[13.387381608026923,52.533025016495436],[13.390151862793777,52.53353630910886],[13.39303289999998,52.5337089528412]]]}
}
```

2. Get a list of restaurants: `GET` to `/restaurants/`. Response will be in GeoJSON format:

```
{
    "type": "FeatureCollection",
    "features": [
        {
            "id": 47,
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [
                            13.39804260000005,
                            52.54958265284123
                        ],
                        [
                            13.40092451369164,
                            52.54941000909199
                        ],
                        [
                            13.403695611209237,
                            52.548898716430486
                        ],
                        [
                            13.406249345014139,
                            52.54806843489111
                        ],
                        [
                            13.40848753926724,
                            52.54695108870388
                        ],
                        [
                            13.410324168347941,
                            52.545589636878056
                        ],
                        [
                            13.4116886647568,
                            52.54403641926164
                        ],
                        [
                            13.412528628979953,
                            52.54235114210205
                        ],
                        [
                            13.412811837484181,
                            52.540598580985844
                        ],
                        [
                            13.41252747254516,
                            52.53884608982543
                        ],
                        [
                            13.411686527943901,
                            52.53716101188306
                        ],
                        [
                            13.410321376467296,
                            52.5356080924163
                        ],
                        [
                            13.408484517357346,
                            52.53424699228197
                        ],
                        [
                            13.406246553133379,
                            52.533129997786254
                        ],
                        [
                            13.403693474396178,
                            52.53230001439654
                        ],
                        [
                            13.400923357256731,
                            52.53178892095227
                        ],
                        [
                            13.39804260000005,
                            52.53161634715884
                        ],
                        [
                            13.395161842743368,
                            52.53178892095227
                        ],
                        [
                            13.392391725603922,
                            52.53230001439654
                        ],
                        [
                            13.389838646866721,
                            52.533129997786254
                        ],
                        [
                            13.387600682642754,
                            52.53424699228197
                        ],
                        [
                            13.385763823532804,
                            52.5356080924163
                        ],
                        [
                            13.384398672056196,
                            52.53716101188306
                        ],
                        [
                            13.38355772745494,
                            52.53884608982543
                        ],
                        [
                            13.383273362515919,
                            52.540598580985844
                        ],
                        [
                            13.383556571020147,
                            52.54235114210205
                        ],
                        [
                            13.3843965352433,
                            52.54403641926164
                        ],
                        [
                            13.385761031652159,
                            52.545589636878056
                        ],
                        [
                            13.38759766073286,
                            52.54695108870388
                        ],
                        [
                            13.38983585498596,
                            52.54806843489111
                        ],
                        [
                            13.392389588790863,
                            52.548898716430486
                        ],
                        [
                            13.39516068630846,
                            52.54941000909199
                        ],
                        [
                            13.39804260000005,
                            52.54958265284123
                        ]
                    ]
                ]
            },
            "properties": {
                "name": "Papa Johns",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        52.53807949999999,
                        13.39552260000005
                    ]
                }
            }
        }
    ]
}
```

3. Optimize restaurant polygons: `POST` to `/restaurants/optimize/`.
