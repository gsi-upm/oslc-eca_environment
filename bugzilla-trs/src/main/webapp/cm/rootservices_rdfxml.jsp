<?xml version="1.0" encoding="UTF-8"?>
<%--
 Copyright (c) 2011, 2013 IBM Corporation.

 All rights reserved. This program and the accompanying materials
 are made available under the terms of the Eclipse Public License v1.0
 and Eclipse Distribution License v. 1.0 which accompanies this distribution.
 
 The Eclipse Public License is available at http://www.eclipse.org/legal/epl-v10.html
 and the Eclipse Distribution License is available at
 http://www.eclipse.org/org/documents/edl-v10.php.
 
 Contributors:
 
    Sam Padgett		 - initial API and implementation
    Michael Fiedler	 - adapted for OSLC4J
--%>
<%@ page contentType="application/rdf+xml" language="java" pageEncoding="UTF-8" %>
<%
String baseUri = (String) request.getAttribute("baseUri");
String catalogUri = (String) request.getAttribute("catalogUri");
String oauthDomain = (String) request.getAttribute("oauthDomain");
String about = (String) request.getAttribute("about");
%>
<!-- Jazz Root Services, see:
	https://jazz.net/wiki/bin/view/Main/RootServicesSpec
	https://jazz.net/wiki/bin/view/Main/RootServicesSpecAddendum2
 -->
<rdf:Description rdf:about="<%= about %>"
	xmlns:bugz="http://www.bugzilla.org/rdf#"
	xmlns:trs="http://open-services.net/ns/core/trs#"
    xmlns:oslc_cm="http://open-services.net/xmlns/cm/1.0/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:jfs="http://jazz.net/xmlns/prod/jazz/jfs/1.0/" 
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

	<dcterms:title>OSLC-CM Adapter/Bugzilla Jazz Root Services</dcterms:title>
	<oslc_cm:cmServiceProviders rdf:resource="<%= catalogUri %>" />
	<jfs:oauthRealmName>Bugzilla</jfs:oauthRealmName>
	<jfs:oauthDomain><%= oauthDomain %></jfs:oauthDomain>
	<jfs:oauthRequestConsumerKeyUrl rdf:resource="<%= baseUri + "/oauth/requestKey" %>" />
	<jfs:oauthApprovalModuleUrl rdf:resource="<%= baseUri + "/oauth/approveKey" %>" />
	<jfs:oauthRequestTokenUrl rdf:resource="<%= baseUri + "/oauth/requestToken" %>"/>
	<jfs:oauthUserAuthorizationUrl rdf:resource="<%= baseUri + "/oauth/authorize" %>" />
	<jfs:oauthAccessTokenUrl rdf:resource="<%= baseUri + "/oauth/accessToken" %>"/>
<%-- Added in Lab 1.1 --%>
	<!-- Bugzilla Tracked Resource Set Provider -->
	<bugz:trackedResourceSetProvider>
		<trs:TrackedResourceSetProvider>
			<trs:trackedResourceSet rdf:resource="<%= baseUri + "/trs" %>" />
		</trs:TrackedResourceSetProvider>		
	</bugz:trackedResourceSetProvider>
</rdf:Description>
