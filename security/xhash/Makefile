# $NetBSD$

DISTNAME=	xhash-3.6.1
CATEGORIES=	security
MASTER_SITES=	${MASTER_SITE_GITHUB:=ricardobranco777/}
GITHUB_TAG=	v${PKGVERSION_NOREV}

MAINTAINER=	rbranco@suse.de
HOMEPAGE=	https://github.com/ricardobranco777/xhash
COMMENT=	Faster hashing with Goroutines
LICENSE=	mit

GO_VERSION_REQD=	124

.include "go-modules.mk"

.include "../../lang/go/go-module.mk"
.include "../../mk/bsd.pkg.mk"

post-install:
	${CHMOD} go+rx ${DESTDIR}${PREFIX}/bin/xhash
	${CHOWN} ${ROOT_USER} ${DESTDIR}${PREFIX}/bin/xhash
