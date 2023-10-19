# Oref Alert

[![HACS Badge](https://img.shields.io/badge/HACS-Default-31A9F4.svg?style=for-the-badge)](https://github.com/hacs/integration)

[![GitHub Release](https://img.shields.io/github/release/amitfin/oref_alert.svg?style=for-the-badge&color=blue)](https://github.com/amitfin/oref_alert/releases)

![Download](https://img.shields.io/github/downloads/amitfin/oref_alert/total.svg?style=for-the-badge&color=blue) ![Analytics](https://img.shields.io/badge/dynamic/json?style=for-the-badge&color=blue&label=Analytics&suffix=%20Installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.oref_alert.total)

![Project Maintenance](https://img.shields.io/badge/maintainer-Amit%20Finkelstein-blue.svg?style=for-the-badge)

The integrartion provides a single binary sensor: `binary_sensor.oref_alert`. The sensor truns on when an alert is reported by the [Israeli National Emergency Portal](https://www.oref.org.il//12481-he/Pakar.aspx) (Pikud Haoref). The sensor monitors the alerts in the user selected areas. An alert is considered active for a certain period of time as configured by the user (10 minutes by default).
The integraion is installed and configured only via the user interface. There is no YAML or templates involved.

## Install
[HACS](https://hacs.xyz/) is the preferred and easier way to install the component. When HACS is installed, the integration can be installed using this My button:

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=amitfin&repository=oref_alert&category=integration)

Otherwise, download `oref_alert.zip` from the [latest release](https://github.com/amitfin/oref_alert/releases), extract and copy the content under `custom_components` directory.

Home Assistant restart is required once the integration files are copied (either by HACS or manually).

The integration should also be added to the configuration. This can be done via this My button:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=oref_alert)

There are 4 configuration fields, but only the first one doesn't have a good default:
1. Selected areas: list of areas to monitor. The [Israeli National Emergency Portal](https://www.oref.org.il//12481-he/Pakar.aspx) has instructions on how to find an area by supplying an address.
2. Max age of an alert: this is the alert's active time period (in minutes). The default is 10 minutes.
3. On icon: the icon to be used when there are active alerts in one of the selected areas. This is the icon which is displayed when the state of the binary sensor is "on".
4. Off icon: the icon to  be used when the state of the binary sensor is "off".

## Additional Attributes

In addition to the entity's state (on or off), the entity has the following attributes:
1. `Areas`: the list of areas provided by the user.
2. `Alert max age`: as configured by the user.
3. `Selected areas active alerts`: when the sensor is `on`, the alerts are listed here. 
4. `Selected areas alerts`: active and inactive alerts in the selected areas.
5. `Country active alerts`: all active alerts in Israel.
6. `Country alerts`: all alerts in Israel.

## Additional Information

1. The integration monitors the published data every second.
2. The purpose of the binary sensor is to be used by automation rules.
3. For advanced users, it's also possible to use the attributes of the sensor in templates.

## Advanced Scenarios (Templates)

It's possible to use templates for creating additional entities or as conditions in automation rules. _Note: this is not needed for the common use case of running automation rule inside your house when there is an alert in your area._

The basic block is:
```
{{ 'פתח תקווה' in (state_attr('binary_sensor.oref_alert', 'selected_areas_active_alerts') | map(attribute='data')) }}
```
There are 4 state attributes (with identical format) which can be used:
1. `selected_areas_active_alerts`
2. `country_active_alerts`
3. `selected_areas_alerts`
4. `country_alerts`

Here is an example for a binary sensor:
```
template:
  - binary_sensor:
      - name: Petah Tikva Oref Alert
        unique_id: petah_tikva_oref_alret
        state: "{{ 'פתח תקווה' in (state_attr('binary_sensor.oref_alert', 'selected_areas_active_alerts') | map(attribute='data')) }}"
        availability: "{{ has_value('binary_sensor.oref_alert') }}"
```

And here is an example for an automation rule's condition:
```
description: Petah Tikva Alert
trigger:
  - platform: state
    entity_id:
      - binary_sensor.oref_alert
    from: "off"
    to: "on"
condition:
  - condition: template
    value_template: "{{ 'פתח תקווה' in (state_attr('binary_sensor.oref_alert', 'selected_areas_active_alerts') | map(attribute='data')) }}"
action:
...
```

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)
