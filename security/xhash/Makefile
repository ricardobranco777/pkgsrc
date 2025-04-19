# $NetBSD$

DISTNAME=	xhash-3.6.3
CATEGORIES=	security
MASTER_SITES=	${MASTER_SITE_GITHUB:=ricardobranco777/}
GITHUB_TAG=	v${PKGVERSION_NOREV}

MAINTAINER=	rbranco@suse.de
HOMEPAGE=	https://github.com/ricardobranco777/xhash
COMMENT=	Faster hashing with Goroutines
LICENSE=	mit

GO_VERSION_REQD=	124

INSTALLATION_DIRS=	bin ${PKGMANDIR}/man1

.include "go-modules.mk"

.include "../../lang/go/go-module.mk"
.include "../../mk/bsd.pkg.mk"

post-install:
	${CHMOD} go+rx ${DESTDIR}${PREFIX}/bin/xhash
	${CHOWN} ${ROOT_USER} ${DESTDIR}${PREFIX}/bin/xhash
	${INSTALL_MAN} ${WRKSRC}/xhash.1 ${DESTDIR}${PREFIX}/${PKGMANDIR}/man1/xhash.1
