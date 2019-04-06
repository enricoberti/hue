#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2008 Søren Roug, European Environment Agency
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Contributor(s):
#

from odf.namespaces import *

# Inline element don't cause a box
# They are analogous to the HTML elements SPAN, B, I etc.
inline_elements = (
    (TEXTNS,u'a'),
    (TEXTNS,u'author-initials'),
    (TEXTNS,u'author-name'),
    (TEXTNS,u'bibliography-mark'),
    (TEXTNS,u'bookmark-ref'),
    (TEXTNS,u'chapter'),
    (TEXTNS,u'character-count'),
    (TEXTNS,u'conditional-text'),
    (TEXTNS,u'creation-date'),
    (TEXTNS,u'creation-time'),
    (TEXTNS,u'creator'),
    (TEXTNS,u'database-display'),
    (TEXTNS,u'database-name'),
    (TEXTNS,u'database-next'),
    (TEXTNS,u'database-row-number'),
    (TEXTNS,u'database-row-select'),
    (TEXTNS,u'date'),
    (TEXTNS,u'dde-connection'),
    (TEXTNS,u'description'),
    (TEXTNS,u'editing-cycles'),
    (TEXTNS,u'editing-duration'),
    (TEXTNS,u'execute-macro'),
    (TEXTNS,u'expression'),
    (TEXTNS,u'file-name'),
    (TEXTNS,u'hidden-paragraph'),
    (TEXTNS,u'hidden-text'),
    (TEXTNS,u'image-count'),
    (TEXTNS,u'initial-creator'),
    (TEXTNS,u'keywords'),
    (TEXTNS,u'measure'),
    (TEXTNS,u'modification-date'),
    (TEXTNS,u'modification-time'),
    (TEXTNS,u'note-ref'),
    (TEXTNS,u'object-count'),
    (TEXTNS,u'page-continuation'),
    (TEXTNS,u'page-count'),
    (TEXTNS,u'page-number'),
    (TEXTNS,u'page-variable-get'),
    (TEXTNS,u'page-variable-set'),
    (TEXTNS,u'paragraph-count'),
    (TEXTNS,u'placeholder'),
    (TEXTNS,u'print-date'),
    (TEXTNS,u'printed-by'),
    (TEXTNS,u'print-time'),
    (TEXTNS,u'reference-ref'),
    (TEXTNS,u'ruby'),
    (TEXTNS,u'ruby-base'),
    (TEXTNS,u'ruby-text'),
    (TEXTNS,u'script'),
    (TEXTNS,u'sender-city'),
    (TEXTNS,u'sender-company'),
    (TEXTNS,u'sender-country'),
    (TEXTNS,u'sender-email'),
    (TEXTNS,u'sender-fax'),
    (TEXTNS,u'sender-firstname'),
    (TEXTNS,u'sender-initials'),
    (TEXTNS,u'sender-lastname'),
    (TEXTNS,u'sender-phone-private'),
    (TEXTNS,u'sender-phone-work'),
    (TEXTNS,u'sender-position'),
    (TEXTNS,u'sender-postal-code'),
    (TEXTNS,u'sender-state-or-province'),
    (TEXTNS,u'sender-street'),
    (TEXTNS,u'sender-title'),
    (TEXTNS,u'sequence'),
    (TEXTNS,u'sequence-ref'),
    (TEXTNS,u'sheet-name'),
    (TEXTNS,u'span'),
    (TEXTNS,u'subject'),
    (TEXTNS,u'table-count'),
    (TEXTNS,u'table-formula'),
    (TEXTNS,u'template-name'),
    (TEXTNS,u'text-input'),
    (TEXTNS,u'time'),
    (TEXTNS,u'title'),
    (TEXTNS,u'user-defined'),
    (TEXTNS,u'user-field-get'),
    (TEXTNS,u'user-field-input'),
    (TEXTNS,u'variable-get'),
    (TEXTNS,u'variable-input'),
    (TEXTNS,u'variable-set'),
    (TEXTNS,u'word-count'),
)


# It is almost impossible to determine what elements are block elements.
# There are so many that don't fit the form
block_elements = (
    (TEXTNS,u'h'),
    (TEXTNS,u'p'),
    (TEXTNS,u'list'),
    (TEXTNS,u'list-item'),
    (TEXTNS,u'section'),
)

declarative_elements = (
    (OFFICENS,u'font-face-decls'),
    (PRESENTATIONNS,u'date-time-decl'),
    (PRESENTATIONNS,u'footer-decl'),
    (PRESENTATIONNS,u'header-decl'),
    (TABLENS,u'table-template'),
    (TEXTNS,u'alphabetical-index-entry-template'),
    (TEXTNS,u'alphabetical-index-source'),
    (TEXTNS,u'bibliography-entry-template'),
    (TEXTNS,u'bibliography-source'),
    (TEXTNS,u'dde-connection-decls'),
    (TEXTNS,u'illustration-index-entry-template'),
    (TEXTNS,u'illustration-index-source'),
    (TEXTNS,u'index-source-styles'),
    (TEXTNS,u'index-title-template'),
    (TEXTNS,u'note-continuation-notice-backward'),
    (TEXTNS,u'note-continuation-notice-forward'),
    (TEXTNS,u'notes-configuration'),
    (TEXTNS,u'object-index-entry-template'),
    (TEXTNS,u'object-index-source'),
    (TEXTNS,u'sequence-decls'),
    (TEXTNS,u'table-index-entry-template'),
    (TEXTNS,u'table-index-source'),
    (TEXTNS,u'table-of-content-entry-template'),
    (TEXTNS,u'table-of-content-source'),
    (TEXTNS,u'user-field-decls'),
    (TEXTNS,u'user-index-entry-template'),
    (TEXTNS,u'user-index-source'),
    (TEXTNS,u'variable-decls'),
)

empty_elements = (
    (ANIMNS,u'animate'),
    (ANIMNS,u'animateColor'),
    (ANIMNS,u'animateMotion'),
    (ANIMNS,u'animateTransform'),
    (ANIMNS,u'audio'),
    (ANIMNS,u'param'),
    (ANIMNS,u'set'),
    (ANIMNS,u'transitionFilter'),
    (CHARTNS,u'categories'),
    (CHARTNS,u'data-point'),
    (CHARTNS,u'domain'),
    (CHARTNS,u'error-indicator'),
    (CHARTNS,u'floor'),
    (CHARTNS,u'grid'),
    (CHARTNS,u'legend'),
    (CHARTNS,u'mean-value'),
    (CHARTNS,u'regression-curve'),
    (CHARTNS,u'stock-gain-marker'),
    (CHARTNS,u'stock-loss-marker'),
    (CHARTNS,u'stock-range-line'),
    (CHARTNS,u'symbol-image'),
    (CHARTNS,u'wall'),
    (DR3DNS,u'cube'),
    (DR3DNS,u'extrude'),
    (DR3DNS,u'light'),
    (DR3DNS,u'rotate'),
    (DR3DNS,u'sphere'),
    (DRAWNS,u'contour-path'),
    (DRAWNS,u'contour-polygon'),
    (DRAWNS,u'equation'),
    (DRAWNS,u'fill-image'),
    (DRAWNS,u'floating-frame'),
    (DRAWNS,u'glue-point'),
    (DRAWNS,u'gradient'),
    (DRAWNS,u'handle'),
    (DRAWNS,u'hatch'),
    (DRAWNS,u'layer'),
    (DRAWNS,u'marker'),
    (DRAWNS,u'opacity'),
    (DRAWNS,u'page-thumbnail'),
    (DRAWNS,u'param'),
    (DRAWNS,u'stroke-dash'),
    (FORMNS,u'connection-resource'),
    (FORMNS,u'list-value'),
    (FORMNS,u'property'),
    (MANIFESTNS,u'algorithm'),
    (MANIFESTNS,u'key-derivation'),
    (METANS,u'auto-reload'),
    (METANS,u'document-statistic'),
    (METANS,u'hyperlink-behaviour'),
    (METANS,u'template'),
    (NUMBERNS,u'am-pm'),
    (NUMBERNS,u'boolean'),
    (NUMBERNS,u'day'),
    (NUMBERNS,u'day-of-week'),
    (NUMBERNS,u'era'),
    (NUMBERNS,u'fraction'),
    (NUMBERNS,u'hours'),
    (NUMBERNS,u'minutes'),
    (NUMBERNS,u'month'),
    (NUMBERNS,u'quarter'),
    (NUMBERNS,u'scientific-number'),
    (NUMBERNS,u'seconds'),
    (NUMBERNS,u'text-content'),
    (NUMBERNS,u'week-of-year'),
    (NUMBERNS,u'year'),
    (OFFICENS,u'dde-source'),
    (PRESENTATIONNS,u'date-time'),
    (PRESENTATIONNS,u'footer'),
    (PRESENTATIONNS,u'header'),
    (PRESENTATIONNS,u'placeholder'),
    (PRESENTATIONNS,u'play'),
    (PRESENTATIONNS,u'show'),
    (PRESENTATIONNS,u'sound'),
    (SCRIPTNS,u'event-listener'),
    (STYLENS,u'column'),
    (STYLENS,u'column-sep'),
    (STYLENS,u'drop-cap'),
    (STYLENS,u'footnote-sep'),
    (STYLENS,u'list-level-properties'),
    (STYLENS,u'map'),
    (STYLENS,u'ruby-properties'),
    (STYLENS,u'table-column-properties'),
    (STYLENS,u'tab-stop'),
    (STYLENS,u'text-properties'),
    (SVGNS,u'definition-src'),
    (SVGNS,u'font-face-format'),
    (SVGNS,u'font-face-name'),
    (SVGNS,u'stop'),
    (TABLENS,u'body'),
    (TABLENS,u'cell-address'),
    (TABLENS,u'cell-range-source'),
    (TABLENS,u'change-deletion'),
    (TABLENS,u'consolidation'),
    (TABLENS,u'database-source-query'),
    (TABLENS,u'database-source-sql'),
    (TABLENS,u'database-source-table'),
    (TABLENS,u'data-pilot-display-info'),
    (TABLENS,u'data-pilot-field-reference'),
    (TABLENS,u'data-pilot-group-member'),
    (TABLENS,u'data-pilot-layout-info'),
    (TABLENS,u'data-pilot-member'),
    (TABLENS,u'data-pilot-sort-info'),
    (TABLENS,u'data-pilot-subtotal'),
    (TABLENS,u'dependency'),
    (TABLENS,u'error-macro'),
    (TABLENS,u'even-columns'),
    (TABLENS,u'even-rows'),
    (TABLENS,u'filter-condition'),
    (TABLENS,u'first-column'),
    (TABLENS,u'first-row'),
    (TABLENS,u'highlighted-range'),
    (TABLENS,u'insertion-cut-off'),
    (TABLENS,u'iteration'),
    (TABLENS,u'label-range'),
    (TABLENS,u'last-column'),
    (TABLENS,u'last-row'),
    (TABLENS,u'movement-cut-off'),
    (TABLENS,u'named-expression'),
    (TABLENS,u'named-range'),
    (TABLENS,u'null-date'),
    (TABLENS,u'odd-columns'),
    (TABLENS,u'odd-rows'),
    (TABLENS,u'operation'),
    (TABLENS,u'scenario'),
    (TABLENS,u'sort-by'),
    (TABLENS,u'sort-groups'),
    (TABLENS,u'source-range-address'),
    (TABLENS,u'source-service'),
    (TABLENS,u'subtotal-field'),
    (TABLENS,u'table-column'),
    (TABLENS,u'table-source'),
    (TABLENS,u'target-range-address'),
    (TEXTNS,u'alphabetical-index-auto-mark-file'),
    (TEXTNS,u'alphabetical-index-mark'),
    (TEXTNS,u'alphabetical-index-mark-end'),
    (TEXTNS,u'alphabetical-index-mark-start'),
    (TEXTNS,u'bookmark'),
    (TEXTNS,u'bookmark-end'),
    (TEXTNS,u'bookmark-start'),
    (TEXTNS,u'change'),
    (TEXTNS,u'change-end'),
    (TEXTNS,u'change-start'),
    (TEXTNS,u'dde-connection-decl'),
    (TEXTNS,u'index-entry-bibliography'),
    (TEXTNS,u'index-entry-chapter'),
    (TEXTNS,u'index-entry-link-end'),
    (TEXTNS,u'index-entry-link-start'),
    (TEXTNS,u'index-entry-page-number'),
    (TEXTNS,u'index-entry-tab-stop'),
    (TEXTNS,u'index-entry-text'),
    (TEXTNS,u'index-source-style'),
    (TEXTNS,u'line-break'),
    (TEXTNS,u'page'),
    (TEXTNS,u'reference-mark'),
    (TEXTNS,u'reference-mark-end'),
    (TEXTNS,u'reference-mark-start'),
    (TEXTNS,u's'),
    (TEXTNS,u'section-source'),
    (TEXTNS,u'sequence-decl'),
    (TEXTNS,u'soft-page-break'),
    (TEXTNS,u'sort-key'),
    (TEXTNS,u'tab'),
    (TEXTNS,u'toc-mark'),
    (TEXTNS,u'toc-mark-end'),
    (TEXTNS,u'toc-mark-start'),
    (TEXTNS,u'user-field-decl'),
    (TEXTNS,u'user-index-mark'),
    (TEXTNS,u'user-index-mark-end'),
    (TEXTNS,u'user-index-mark-start'),
    (TEXTNS,u'variable-decl')
)
