=========================
Tornado+Sprockets Example
=========================

Example web application that uses the common sprockets in unison to implement a
simple CRUD service.

Sprockets used
==============

* `sprockets.http <https://github.com/sprockets/sprockets.http/>`_
  implements running a tornado application safely.  This is used to implement
  an application runtime that can be used in development (single process with
  debug output) and as a forked daemon that is signal compatible with running
  as a docker container.  It also provides a cleaner default error handling
  behavior for HTTP APIs.
* `sprockets.handlers.status <https://github.com/sprockets/sprockets.handlers.status>`_
  implements a simple request handler that reports the package's name,
  version, and status.
* `sprockets.mixins.mediatype <https://github.com/sprockets/sprockets.mixins.media_type>`_
  implements *proactive content negotiation* as described in section 3.1 of
  `RFC-7231 <https://tools.ietf.org/html/rfc7231#section-3.4.1>`_.
