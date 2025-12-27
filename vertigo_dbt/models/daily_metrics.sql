SELECT
  event_date,
  country,
  platform,
  COUNT(*) AS total_events,
  COUNT(DISTINCT user_id) AS daily_active_users
FROM {{ source('analytics', 'user_events') }}
GROUP BY
  event_date,
  country,
  platform
