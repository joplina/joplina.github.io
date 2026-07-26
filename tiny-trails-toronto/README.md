# Tiny Trails Toronto

A small static website that ranks family walks around Greater Toronto by:

1. child age fit
2. forecast suitability for the specific type of place
3. estimated drive time

It also shows stroller friendliness, surfaces, cautions, cost notes, parking notes, and Google Maps directions.

## Run it

The simplest option is to open `index.html` in a browser. For the most reliable browser location access, run a local web server:

```bash
cd tiny-trails-toronto
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Deploy it

Because this is a single static page, it can be deployed directly to GitHub Pages, Netlify, Cloudflare Pages, or any ordinary web host.

## Data and limitations

- Live forecast and place-name geocoding use Open-Meteo and do not require an API key for this prototype.
- Drive time is an estimate derived from distance and typical urban speeds. It does not include live traffic.
- Google Maps is opened for actual routing.
- The location list is a curated starter dataset. Verify current closures, trail conditions, hours, washrooms, parking, fees, and accessibility before leaving.
- Saved places are stored only in the browser using local storage.

## Easy next upgrades

- Use a routing API for live drive times and traffic.
- Pull park and facility records from Toronto Open Data.
- Add indoor alternatives for rain, snow, smoke, or extreme heat.
- Add a map view and push notifications for ideal outing windows.
- Let an administrator edit locations through a small database instead of changing the HTML.
