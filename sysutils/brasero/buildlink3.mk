# $NetBSD: buildlink3.mk,v 1.74 2024/04/07 07:34:57 wiz Exp $

BUILDLINK_TREE+=	brasero

.if !defined(BRASERO_BUILDLINK3_MK)
BRASERO_BUILDLINK3_MK:=

BUILDLINK_API_DEPENDS.brasero+=	brasero>=3.12.2
BUILDLINK_ABI_DEPENDS.brasero?=	brasero>=3.12.2nb23
BUILDLINK_PKGSRCDIR.brasero?=	../../sysutils/brasero

.include "../../x11/gtk3/buildlink3.mk"
.endif	# BRASERO_BUILDLINK3_MK

BUILDLINK_TREE+=	-brasero
