# Source: https://github.com/onflow/cadence-lang.org/blob/main/src/theme/NotFound.js

```
import React, { useEffect } from 'react';
import NotFound from '@theme-original/NotFound';

export default function NotFoundWrapper(props) {
  useEffect(() => {
    if (typeof window !== 'undefined' && window?.mixpanel) {
      window.mixpanel.track('Page Not Found', {
        'Page URL': window.location.pathname,
      });
    }
  }, []);
  return (
    <>
      <NotFound {...props} />
    </>
  );
}

```