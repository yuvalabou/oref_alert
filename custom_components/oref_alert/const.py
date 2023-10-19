"""Constants for the oref_alert integration."""
import logging
from typing import Final

DOMAIN: Final = "oref_alert"
LOGGER = logging.getLogger(__package__)

ATTR_COUNTRY_ALERTS: Final = "country_alerts"
ATTR_COUNTRY_ACTIVE_ALERTS: Final = "country_active_alerts"
ATTR_SELECTED_AREAS_ALERTS: Final = "selected_areas_alerts"
ATTR_SELECTED_AREAS_ACTIVE_ALERTS: Final = "selected_areas_active_alerts"

CONF_AREAS: Final = "areas"
CONF_ALERT_MAX_AGE: Final = "alert_max_age"
CONF_OFF_ICON: Final = "off_icon"
CONF_ON_ICON: Final = "on_icon"
CONF_POLL_INTERVAL: Final = "poll_interval"

DEFAULT_ALERT_MAX_AGE: Final = 10
DEFAULT_ON_ICON: Final = "mdi:home-alert-outline"
DEFAULT_OFF_ICON: Final = "mdi:home-outline"
DEFAULT_POLL_INTERVAL: Final = 5
