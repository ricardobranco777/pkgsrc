#	$NetBSD: nls.mk,v 1.4 2024/09/17 11:52:28 jperkin Exp $

.if !target(.MAIN)
# init.mk not included
.-include <${.CURDIR:H}/Makefile.inc>

.MAIN: all
.endif

.SUFFIXES: .cat .msg

.msg.cat:
	@rm -f ${.TARGET}
	gencat ${.TARGET} ${.IMPSRC}

.if defined(NLS) && !empty(NLS)
NLSALL= ${NLS:.msg=.cat}
.NOPATH: ${NLSALL}
.endif

.if !defined(NLSNAME)
.if defined(PROG)
NLSNAME=${PROG}
.else
NLSNAME=lib${LIB}
.endif
.endif

nlsinstall:
.if defined(NLSALL)
	@for msg in ${NLSALL}; do \
		NLSLANG=`basename $$msg .cat`; \
		dir=${DESTDIR}${NLSDIR}/$${NLSLANG}; \
		${INSTALL} -d $$dir; \
		${INSTALL} ${COPY} -o ${NLSOWN} -g ${NLSGRP} -m ${NLSMODE} $$msg $$dir/${NLSNAME}.cat; \
	done
.endif

.if defined(NLSALL)
all: ${NLSALL}

install:  nlsinstall

cleandir: cleannls
cleannls:
	rm -f ${NLSALL}
.endif
