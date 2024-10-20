# $NetBSD: options.mk,v 1.4 2024/07/02 13:13:25 mef Exp $

PKG_OPTIONS_VAR=	PKG_OPTIONS.emacs-w3m
PKG_SUPPORTED_OPTIONS=	emacs-w3m-mew

.include "../../mk/bsd.options.mk"

PLIST_VARS+=	mew

# xemacs-packages contain mew (but not mew-nntp)
.if (${EMACS_FLAVOR} == "xemacs")
PLIST.mew=	yes
.elif !empty(PKG_OPTIONS:Memacs-w3m-mew)
.include "../../mail/mew/buildlink3.mk"
PLIST.mew=	yes
.endif
