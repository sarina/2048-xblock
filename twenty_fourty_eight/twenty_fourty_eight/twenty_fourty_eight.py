"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class TwentyFourtyEightXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the TwentyFourtyEightXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/twenty_fourty_eight.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/twenty_fourty_eight.css"))
        frag.add_css(self.resource_string("static/css/main.css"))

        frag.add_javascript(self.resource_string("static/js/src/twenty_fourty_eight.js"))
        frag.add_javascript(self.resource_string("static/js/src/animframe_polyfill.js"))
        frag.add_javascript(self.resource_string("static/js/src/application.js"))
        frag.add_javascript(self.resource_string("static/js/src/bind_polyfill.js"))
        frag.add_javascript(self.resource_string("static/js/src/classlist_polyfill.js"))
        frag.add_javascript(self.resource_string("static/js/src/game_manager.js"))
        frag.add_javascript(self.resource_string("static/js/src/grid.js"))
        frag.add_javascript(self.resource_string("static/js/src/html_actuator.js"))
        frag.add_javascript(self.resource_string("static/js/src/keyboard_input_manager.js"))
        frag.add_javascript(self.resource_string("static/js/src/local_storage_manager.js"))
        frag.add_javascript(self.resource_string("static/js/src/tile.js"))
        frag.initialize_js('TwentyFourtyEightXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("TwentyFourtyEightXBlock",
             """<vertical_demo>
                <twenty_fourty_eight/>
                </vertical_demo>
             """),
        ]
