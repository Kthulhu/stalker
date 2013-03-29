# -*- coding: utf-8 -*-
# Copyright (c) 2009-2013, Erkan Ozgur Yilmaz
# 
# This module is part of Stalker and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

from pyramid.httpexceptions import HTTPServerError
from pyramid.security import authenticated_userid
from pyramid.view import view_config
from sqlalchemy.exc import IntegrityError
import transaction

from stalker.db import DBSession
from stalker import User, Sequence, StatusList, Status, Shot, Project

import logging
from stalker import log
logger = logging.getLogger(__name__)
logger.setLevel(log.logging_level)


@view_config(
    route_name='add_shot',
    renderer='templates/shot/add_shot.jinja2',
    permission='Add_Shot'
)
def add_shot(request):
    """runs when adding a new shot
    """
    login = authenticated_userid(request)
    logged_in_user = User.query.filter_by(login=login).first()
    
    if 'submitted' in request.params:
        logger.debug('request.params["submitted"]: %s' % request.params['submitted'])
        
        if request.params['submitted'] == 'add':
            if 'name' in request.params and \
               'code' in request.params and  \
               'sequence_id' in request.params and \
               'status_list_id' in request.params and \
               'status_id' in request.params:
                
                sequence_id = request.params['sequence_id']
                sequence = Sequence.query.filter_by(id=sequence_id).first()

                project_id = request.matchdict['project_id']
                project = Project.query.filter_by(id=project_id).first()
                # get the status_list
                status_list = StatusList.query.filter_by(
                    id=request.params["status_list_id"]
                ).first()
                
                # there should be a status_list
                if status_list is None:
                    return HTTPServerError(
                        detail='No StatusList found'
                    )
                
                status_id = int(request.params['status_id'])
                status = Status.query.filter_by(id=status_id).first()
                
                # get the info
                try:
                    new_shot = Shot(
                        name=request.params['name'],
                        code=request.params['code'],
                        sequence=sequence,
                        status_list=status_list,
                        status=status,
                        created_by=logged_in_user,
                        project=project
                    )
                    
                    DBSession.add(new_shot)
                except (AttributeError, TypeError) as e:
                    logger.debug(e.message)
                else:
                    DBSession.add(new_shot)
                    try:
                        transaction.commit()
                    except IntegrityError as e:
                        logger.debug(e.message)
                        transaction.abort()
                    else:
                        logger.debug('flushing the DBSession, no problem here!')
                        DBSession.flush()
                        logger.debug('finished adding Shot')
            else:
                logger.debug('there are missing parameters')
                def get_param(param):
                    if param in request.params:
                        logger.debug('%s: %s' % (param, request.params[param]))
                    else:
                        logger.debug('%s not in params' % param)
                get_param('project_id')

    project = Project.query.filter_by(id=request.matchdict['project_id']).first()

    return {
        'project': project,
        'projects': Project.query.all(),
        'status_list':
            StatusList.query.filter_by(target_entity_type='Shot').first()
    }


@view_config(
    route_name='get_shots',
    renderer='json',
    permission='View_Shot'
)
def get_shots(request):
    """returns all the Shots of the given Project
    """
    project_id = request.matchdict['project_id']
    project = Project.query.filter_by(id=project_id).first()
    return [
        {
            'shot': shot,
            'id': shot.id,
            'name': shot.name,
            'project': shot.project,
            'sequences': shot.sequences,
            'status': shot.status.name,
            'user_name': shot.created_by.name
        }
        for shot in Shot.query.filter_by(_project=project).all()
    ]