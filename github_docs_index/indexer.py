"""
The latest version of this package is available at:
<http://github.com/jantman/github-docs-index>

##################################################################################
Copyright 2018 Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>

    This file is part of github-docs-index, also known as github-docs-index.

    github-docs-index is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    github-docs-index is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with github-docs-index.  If not, see <http://www.gnu.org/licenses/>.

The Copyright and Authors attributions contained herein may not be removed or
otherwise altered, except to add the Author attribution of a contributor to
this work. (Additional Terms pursuant to Section 7b of the AGPL v3)
##################################################################################
While not legally required, I sincerely request that anyone who finds
bugs please submit them at <https://github.com/jantman/github-docs-index> or
to me via email, and that you send any contributions or improvements
either as a pull request on GitHub, or to me via email.
##################################################################################

AUTHORS:
Jason Antman <jason@jasonantman.com> <http://www.jasonantman.com>
##################################################################################
"""


class Config(object):
    """
    parse the YAML config file, validate it, and present a simple
    interface to it
    """
    pass


class RepoLink(object):
    """
    Represents one repository that should be linked to in the docs index.
    """

    @property
    def lower_case_name(self):
        pass

    @property
    def last_commit_date(self):
        pass

    @property
    def title(self):
        pass

    @property
    def description(self):
        pass

    @property
    def url(self):
        pass


class GithubInstance(object):
    """
    Represents a distinct GitHub instance that we want to find docs on.
    """

    def __init__(self, url, token, org_or_user_names,
                 blacklist_repos=[], whitelist_repos=[]):
        pass

    def get_docs_repos(self):
        """
        iterate over each org
        for each org, iterate over each repo not in blacklist, or if
           whitelist is specified, only those repos.
        create RepoLink instances for each repo that matches our criteria.
        return the list of RepoLink instances
        """
        pass

class GithubDocsIndexer(object):

    def generate_index(self):
        """
        First generate the skeleton of the index including quick links.
        Construct a GithubInstance for each github we want to check, call
           get_docs_repos() for them, build a list of all of them.
        Add those lists to the index doc, sorted as requested.
        Return the doc, or some representation of it.
        """
        pass
