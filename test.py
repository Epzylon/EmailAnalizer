#/usr/bin/env python3
from HeaderAnalizer.HeaderAnalizer import HeaderAnalizer as HA
from TokenAnalizer.Trace.received import ExtendedDomain as ED
from TokenAnalizer.Trace.received import Received as REC


r_list = ['by 10.35.47.11 with SMTP id z11cs40515pyj; Sat, 25 Feb 2006 11:36:55 -0800 (PST)',
          'by 10.35.70.17 with SMTP id x17mr1433276pyk; Sat, 25 Feb 2006 11:36:55 -0800 (PST)',
          'from hotmail.com (bay116-f5.bay116.hotmail.com [64.4.38.15]) by mx.gmail.com with ESMTP id m78si109227pye.2006.02.25.11.36.54; Sat, 25 Feb 2006 11:36:55 -0800 (PST)',
          'from mail pickup service by hotmail.com with Microsoft SMTPSVC; Sat, 25 Feb 2006 11:36:54 -0800',
          'from 64.4.38.200 by by116fd.bay116.hotmail.msn.com with HTTP; Sat, 25 Feb 2006 19:36:49 GMT',
          'by 10.38.65.42 with SMTP id n42cs9139rna; Wed, 2 Mar 2005 19:07:32 -0800 (PST)', 
          'by 10.38.78.48 with SMTP id a48mr161899rnb; Wed, 02 Mar 2005 19:07:04 -0800 (PST)',
          'from hotmail.com (bay20-f20.bay20.hotmail.com [64.4.54.109]) by mx.gmail.com with ESMTP id 70si602905rnc.2005.03.02.19.07.03; Wed, 02 Mar 2005 19:07:04 -0800 (PST)',
          'from mail pickup service by hotmail.com with Microsoft SMTPSVC; Wed, 2 Mar 2005 19:07:00 -0800',
          'from 200.42.151.206 by by20fd.bay20.hotmail.msn.com with HTTP;\n\tThu, 03 Mar 2005 03:06:45 GMT',
          'by 10.38.65.42 with SMTP id n42cs39675rna; Mon, 21 Mar 2005 15:04:19 -0800 (PST)',
          'by 10.38.206.58 with SMTP id d58mr2008218rng; Mon, 21 Mar 2005 15:04:19 -0800 (PST)',
          'from alemania.dattaweb.com ([200.58.112.83]) by mx.gmail.com with ESMTP id 72si448101rna.2005.03.21.15.04.15; Mon, 21 Mar 2005 15:04:19 -0800 (PST)',
          'from [200.55.118.90] (helo=[192.168.0.1]) by alemania.dattaweb.com with asmtp (Exim 4.30) id 1DDVrR-00076x-9D; Mon, 21 Mar 2005 19:59:01 -0300',
          'by 10.35.47.11 with SMTP id z11cs12825pyj; Tue, 7 Mar 2006 17:25:06 -0800 (PST)',
          'by 10.70.105.2 with SMTP id d2mr244904wxc; Tue, 07 Mar 2006 17:25:05 -0800 (PST)',
          'from server1.desikal.com.ar ([200.69.135.245]) by mx.gmail.com with ESMTP id i37si312211wxd.2006.03.07.17.25.05; Tue, 07 Mar 2006 17:25:05 -0800 (PST)',
          'from apache by server1.desikal.com.ar with local (Exim 4.51) id 1FGnPw-0005cA-Vc\n\tfor lord.epzylon@gmail.com; Tue, 07 Mar 2006 22:24:45 -0300',
          'by 10.38.65.42 with SMTP id n42cs2719rna; Wed, 30 Mar 2005 05:03:19 -0800 (PST)',
          'by 10.54.37.51 with SMTP id k51mr414622wrk; Wed, 30 Mar 2005 05:03:19 -0800 (PST)',
          'from www.no-ip.com (www.no-ip.com [8.4.112.112]) by mx.gmail.com with SMTP id 45si504265wri.2005.03.30.05.03.18; Wed, 30 Mar 2005 05:03:19 -0800 (PST)',
          '(qmail 19640 invoked from network); 30 Mar 2005 13:02:21 -0000',
          'from unknown (HELO bf.vitalwerks.com) (127.0.0.1)  by bf.vitalwerks.com with SMTP; 30 Mar 2005 13:02:21 -0000',
          'by 10.76.27.1 with SMTP id p1csp2517416oag;\n        Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'from mail-io0-x232.google.com (mail-io0-x232.google.com. [2607:f8b0:4001:c06::232]) by mx.google.com with ESMTPS id 199si1933561ioz.26.2016.02.24.03.52.42 for <lord.epzylon@gmail.com> (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128); Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'by mail-io0-x232.google.com with SMTP id g203so19343732iof.2 for <lord.epzylon@gmail.com>; Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'by 10.107.156.10 with HTTP; Wed, 24 Feb 2016 03:52:12 -0800 (PST)',
          'by 10.76.27.1 with SMTP id p1csp1274646oag; Fri, 11 Mar 2016 12:02:09 -0800 (PST)',
          'from mail-lb0-x235.google.com (mail-lb0-x235.google.com. [2a00:1450:4010:c04::235])  by mx.google.com with ESMTPS id l5si4452358lbd.164.2016.03.11.12.02.08 for <lord.epzylon@gmail.com> (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128); Fri, 11 Mar 2016 12:02:09 -0800 (PST)',
          'by mail-lb0-x235.google.com with SMTP id xr8so154340295lbb.1 for <lord.epzylon@gmail.com>; Fri, 11 Mar 2016 12:02:08 -0800 (PST)',
          'by 10.112.126.69 with HTTP; Fri, 11 Mar 2016 12:01:49 -0800 (PST)',
          'by 10.36.7.7 with SMTP id 7cs1838nzg; Mon, 27 Jun 2005 19:08:38 -0700 (PDT)',
          'by 10.54.5.47 with SMTP id 47mr3861468wre; Mon, 27 Jun 2005 19:08:38 -0700 (PDT)',
          'from push.mailxmail.com ([194.116.240.67])  by mx.gmail.com with ESMTP id d75si8569593wra.2005.06.27.19.08.36; Mon, 27 Jun 2005 19:08:38 -0700 (PDT)',
          'from push-mxm (localhost [127.0.0.1]) by push.mailxmail.com (Postfix) with ESMTP id F1A7C4E0031 for <lord.epzylon@gmail.com>; Tue, 28 Jun 2005 04:09:11 +0200 (CEST)',
          'by 10.76.27.1 with SMTP id p1csp19030oag; Fri, 4 Mar 2016 06:45:33 -0800 (PST)',
          'from mailsrv4759.o-mx.com (mailsrv4759.o-mx.com. [205.162.47.59]) by mx.google.com with ESMTP id l15si5187430ioe.169.2016.03.04.06.45.33 for <lord.epzylon@gmail.com>; Fri, 04 Mar 2016 06:45:33 -0800 (PST)',
          'by 10.70.47.101 with SMTP id c5csp78259pdn; Fri, 24 Apr 2015 14:11:52 -0700 (PDT)',
          'from mail.vicarious.com.ar (vicarious.com.ar. [87.98.129.123]) by mx.google.com with ESMTP id ea6si765233wib.98.2015.04.24.14.11.50 for <lord.epzylon@gmail.com>; Fri, 24 Apr 2015 14:11:51 -0700 (PDT)',
          'from gantrithor.vicarious.com.ar (localhost [127.0.0.1]) by mail.vicarious.com.ar (Postfix) with ESMTP id C10AA226DA for <lord.epzylon@gmail.com>; Fri, 24 Apr 2015 18:13:27 -0300 (ART)',
          'by 10.76.27.1 with SMTP id p1csp79020oag; Fri, 4 Mar 2016 08:42:13 -0800 (PST)',
          'from mail-io0-x22e.google.com (mail-io0-x22e.google.com. [2607:f8b0:4001:c06::22e]) by mx.google.com with ESMTPS id w5si3743633igl.90.2016.03.04.08.42.13 for <lord.epzylon@gmail.com> (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);  Fri, 04 Mar 2016 08:42:13 -0800 (PST)',
          'by mail-io0-x22e.google.com with SMTP id g203so59677000iof.2 for <lord.epzylon@gmail.com>; Fri, 04 Mar 2016 08:42:13 -0800 (PST)',
          'by 10.107.32.138 with HTTP; Fri, 4 Mar 2016 08:41:53 -0800 (PST)',
          'by 10.35.47.11 with SMTP id z11cs10877pyj; Wed, 5 Apr 2006 13:25:28 -0700 (PDT)',
          'by 10.36.128.18 with SMTP id a18mr48880nzd; Wed, 05 Apr 2006 13:25:28 -0700 (PDT)',
          'from mail5.zoneedit.com (mail5.zoneedit.com [216.55.181.47]) by mx.gmail.com with ESMTP id 38si1614769nza.2006.04.05.13.25.27; Wed, 05 Apr 2006 13:25:28 -0700 (PDT)',
          'from enlasaty.com.ar (unknown [200.59.10.129]) by mail5.zoneedit.com (Postfix) with SMTP id 749374AE2CE for <lord@epzylon.com.ar>; Wed,  5 Apr 2006 16:27:36 -0400 (EDT)',
          '(qmail 24215 invoked from network); 6 Apr 2006 01:38:20 -0000',
          'from unknown (HELO [192.168.1.2]) (192.168.1.2)\n  by enlasat6.enlasaty.com.ar (192.168.1.200) with ESMTP; 06 Apr 2006 01:38:20 -0000',
          'by 10.78.16.9 with SMTP id 9cs23262hup; Wed, 21 Jun 2006 17:44:37 -0700 (PDT)',
          'by 10.36.77.2 with SMTP id z2mr474835nza; Wed, 21 Jun 2006 17:44:37 -0700 (PDT)',
          'from hotmail.com (bay21-f2.bay21.hotmail.com [65.54.233.91]) by mx.gmail.com with ESMTP id 5si1767258nzk.2006.06.21.17.44.37; Wed, 21 Jun 2006 17:44:37 -0700 (PDT)',
          'from mail pickup service by hotmail.com with Microsoft SMTPSVC; Wed, 21 Jun 2006 17:44:36 -0700',
          'from 201.255.146.160 by by21fd.bay21.hotmail.msn.com with HTTP;\n\tThu, 22 Jun 2006 00:44:35 GMT',
          'by 10.70.47.101 with SMTP id c5csp2520870pdn; Wed, 15 Apr 2015 06:01:57 -0700 (PDT)',
          'from mx32.h.outbound.createsend.com (mx32.h.outbound.createsend.com. [204.75.142.32]) by mx.google.com with ESMTP id 65si3801867iom.65.2015.04.15.06.01.57 for <lord.epzylon@gmail.com>; Wed, 15 Apr 2015 06:01:57 -0700 (PDT)',
          'by 10.76.27.1 with SMTP id p1csp2517416oag; Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'from mail-io0-x232.google.com (mail-io0-x232.google.com. [2607:f8b0:4001:c06::232]) by mx.google.com with ESMTPS id 199si1933561ioz.26.2016.02.24.03.52.42 for <lord.epzylon@gmail.com> (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128); Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'by mail-io0-x232.google.com with SMTP id g203so19343732iof.2 for <lord.epzylon@gmail.com>; Wed, 24 Feb 2016 03:52:42 -0800 (PST)',
          'by 10.107.156.10 with HTTP; Wed, 24 Feb 2016 03:52:12 -0800 (PST)' ]

for r in r_list:
    received = REC(r)
    print(received)

    
    